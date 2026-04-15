const GIST_ID = process.env.GIST_ID;
const GITHUB_TOKEN = process.env.GITHUB_TOKEN;
const FILE_NAME = 'slide-positions.json';

const GH_HEADERS = {
    Authorization: `token ${GITHUB_TOKEN}`,
    'Content-Type': 'application/json',
    Accept: 'application/vnd.github.v3+json',
    'User-Agent': 'seminar-slides-v3',
};

export default async function handler(req, res) {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

    if (req.method === 'OPTIONS') return res.status(200).end();

    if (!GIST_ID || !GITHUB_TOKEN) {
        return res.status(500).json({ error: 'GIST_ID or GITHUB_TOKEN not set' });
    }

    if (req.method === 'GET') {
        const r = await fetch(`https://api.github.com/gists/${GIST_ID}`, { headers: GH_HEADERS });
        if (!r.ok) return res.status(200).json({});
        const gist = await r.json();
        const content = gist.files?.[FILE_NAME]?.content || '{}';
        try {
            return res.status(200).json(JSON.parse(content));
        } catch {
            return res.status(200).json({});
        }
    }

    if (req.method === 'POST') {
        const positions = req.body;
        const r = await fetch(`https://api.github.com/gists/${GIST_ID}`, {
            method: 'PATCH',
            headers: GH_HEADERS,
            body: JSON.stringify({
                files: { [FILE_NAME]: { content: JSON.stringify(positions) } },
            }),
        });
        if (!r.ok) {
            const err = await r.text();
            return res.status(500).json({ error: err });
        }
        return res.status(200).json({ ok: true });
    }

    res.status(405).end();
}
