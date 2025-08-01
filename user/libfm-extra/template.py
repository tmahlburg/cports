pkgname = "libfm-extra"
pkgver = "1.4.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-extra-only" , "--with-gtk=no", "--disable-static"]
hostmakedepends = [
    "automake",
    "gtk-doc-tools",
    "intltool",
    "libtool",
    "pkgconf",
]
makedepends = [
    "gettext-devel",
    "glib-devel",
]
pkgdesc = "Lib providing some file management utilities"
license = "GPL-2.0-or-later"
url = "https://github.com/lxde/libfm"
source = f"https://github.com/lxde/libfm/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "7d7b616411992389a4b7f35796109d605f30bc2ceab84d4081d1665254ebbf82"

@subpackage("libfm-extra-devel")
def _(self):
    return self.default_devel()
