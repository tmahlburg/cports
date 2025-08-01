pkgname = "menu-cache"
pkgver = "1.1.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
hostmakedepends = [
    "automake",
    "gtk-doc-tools",
    "libtool",
    "pkgconf",
]
makedepends = [
    "libfm-extra-devel",
]
pkgdesc = "Lib providing some file management utilities"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxde/menu-cache"
source = f"https://github.com/lxde/menu-cache/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e8af90467df271c3c8700c840ca470ca2915699c6f213c502a87d74608748f08"

@subpackage("menu-cache-devel")
def _(self):
    return self.default_devel()
