pkgname = "helix"
pkgver = "25.01.1"
pkgrel = 1
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "git"]
makedepends = ["rust-std"]
pkgdesc = "Fast modal terminal-based text editor"
license = "MPL-2.0"
url = "https://github.com/helix-editor/helix"
source = f"{url}/releases/download/{pkgver}/helix-{pkgver}-source.tar.xz"
sha256 = "12508c4f5b9ae6342299bd40d281cd9582d3b51487bffe798f3889cb8f931609"
env = {"HELIX_DEFAULT_RUNTIME": "/usr/lib/helix/runtime"}

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def post_prepare(self):
    from cbuild.util import cargo

    cargo.clear_vendor_checksums(self, "cc")


def install(self):
    self.cargo.install(wrksrc="helix-term")
    runtime_dir = "usr/lib/helix/runtime"
    self.install_dir(runtime_dir)

    self.install_files("runtime/queries", runtime_dir)
    self.install_files("runtime/themes", runtime_dir)
    self.install_file("runtime/tutor", runtime_dir)
    self.install_file(
        "runtime/grammars/*.so",
        f"{runtime_dir}/grammars",
        mode=0o755,
        glob=True,
    )

    self.install_completion("contrib/completion/hx.bash", "bash", "hx")
    self.install_completion("contrib/completion/hx.fish", "fish", "hx")
    self.install_completion("contrib/completion/hx.zsh", "zsh", "hx")

    self.install_file(f"contrib/{pkgname}.png", "usr/share/pixmaps")
    self.install_file("contrib/Helix.desktop", "usr/share/applications")
