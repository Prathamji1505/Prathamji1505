# Profile identity assets

Updated on 7 November 2026 at Pratham Sengar's request: use the same cat as the GitHub profile picture and keep the presentation mysterious.

## Cat photograph

assets/cat-portrait.png is the exact existing profile photograph downloaded from https://avatars.githubusercontent.com/u/330995804?v=4&s=800 and reused at the owner's explicit request. The cat, pose, expression, fur, existing appearance, crop, and photographic pixels are unchanged. Only origin metadata is added. The existing GitHub avatar is unchanged. No AI-generated replacement cat is used in the shipped design.

## Mastheads

assets/profile-cat-desktop.png and assets/profile-cat-mobile.png are lossless browser renderings of the outlined lettering, solid dark fields, and the exact source photo composed by tools/build_assets.py. Both carry origin receipts. The desktop is 1600 × 580; the mobile composition is 800 × 900. Native README content is unchanged apart from image paths and alternative text.

## Typography and rebuilding

Bricolage Grotesque remains under SIL OFL, with its original notice in licenses/BricolageGrotesque-OFL.txt. The pinned font source is https://github.com/google/fonts/blob/6ce172f74aa355ea43eb964fa4a91570a4d3064d/ofl/bricolagegrotesque/BricolageGrotesque%5Bopsz%2Cwdth%2Cwght%5D.ttf.

Download the font to .local/fonts/BricolageGrotesque.ttf, install tools/requirements.txt into .local/lib, and run python tools/build_assets.py. Render the two SVG intermediates in .local/masters/ at their exact viewBox sizes to the corresponding PNG paths under assets/. The intermediates reference the local source photo, so render them from their generated location. Keep their origin metadata and update assets/manifest.json. Intermediates stay ignored to avoid duplicating the photograph throughout the repository.
