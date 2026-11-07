"""Create an empty practice folder. Never generates a solution or claims a pass."""
import argparse
import re
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent


def create(platform, slug, language, url='', root=ROOT):
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug):
        raise ValueError('Use a short lowercase slug containing letters, numbers and hyphens')
    if platform not in {'leetcode', 'coderbyte', 'sql', 'fundamentals'}:
        raise ValueError('Unknown practice category')
    if language not in {'javascript', 'python', 'sql'}:
        raise ValueError('Choose javascript, python or sql')
    if (platform == 'sql') != (language == 'sql'):
        raise ValueError('Use --language sql for the sql category only')
    if url:
        parsed = urlsplit(url)
        if parsed.scheme != 'https' or parsed.username or parsed.password:
            raise ValueError('Use a public HTTPS practice link')
        if parsed.query or parsed.fragment or re.search(r'assessment|candidate|invite|token', parsed.path, re.I):
            raise ValueError('Use a public problem link, not an assessment or access link')
        expected = {'leetcode': {'leetcode.com', 'www.leetcode.com'}, 'coderbyte': {'coderbyte.com', 'www.coderbyte.com'}}
        if platform in expected and parsed.hostname not in expected[platform]:
            raise ValueError('The link does not match the selected practice platform')
    base = root / platform
    if platform == 'coderbyte':
        base = base / 'practice' / language
    elif platform == 'sql':
        base = base / 'practice'
    else:
        base = base / language
    target = base / slug
    target.mkdir(parents=True, exist_ok=False)
    ext = {'javascript': 'js', 'python': 'py', 'sql': 'sql'}[language]
    comment = {'javascript': '//', 'python': '#', 'sql': '--'}[language]
    (target / ('attempt.' + ext)).write_text(comment + ' Write your independent attempt here.\n', encoding='utf-8')
    (target / 'README.md').write_text(
        '# ' + slug.replace('-', ' ').title() + '\n\n'
        'Status: Not started\n\nSource: ' + (url or 'Add the public practice link or describe the original task.') + '\n\n'
        '## My summary\n\nDescribe the task in my own words.\n\n'
        '## Approach before coding\n\nNot recorded yet.\n\n'
        '## Explanation and complexity\n\nNot reviewed yet.\n\n'
        '## Checks actually run\n\nNo checks recorded. Include inputs, expected results, commands and actual output.\n\n'
        '## Assistance\n\nRecord docs, hints and AI help used.\n\n'
        '## Later retry\n\nNot attempted yet.\n', encoding='utf-8')
    return target


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('platform', choices=['leetcode', 'coderbyte', 'sql', 'fundamentals'])
    parser.add_argument('slug')
    parser.add_argument('--language', choices=['javascript', 'python', 'sql'], default='javascript')
    parser.add_argument('--url', default='')
    args = parser.parse_args()
    try:
        print(create(args.platform, args.slug, args.language, args.url))
    except (ValueError, FileExistsError) as error:
        parser.exit(1, str(error) + '\n')
