from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "pages"


def test_site_pages_use_shared_stylesheet_and_navigation():
    for name in ["index.html", "security.html", "vpn.html"]:
        html = (PAGES / name).read_text(encoding="utf-8")
        assert 'href="styles.css"' in html
        assert 'class="topbar"' in html
        assert "BEDROCK WALL" in html


def test_site_styles_use_bedrock_texture():
    css = (PAGES / "styles.css").read_text(encoding="utf-8")
    assert "../resources/bedrock_texture.png" in css


def test_vpn_page_keeps_fetch_controls():
    html = (PAGES / "vpn.html").read_text(encoding="utf-8")
    assert "Fetch Available Connections" in html
    assert "parseConnections" in html


def test_site_pages_do_not_link_directly_to_local_exe():
    for name in ["index.html", "security.html", "vpn.html"]:
        html = (PAGES / name).read_text(encoding="utf-8")
        assert 'href="../dist-new/BedrockWallApp.exe"' not in html
