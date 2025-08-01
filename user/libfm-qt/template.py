pkgname = "libfm-qt"
pkgver = "2.2.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "lxqt-build-tools",
    "ninja",
    "perl",
    "pkgconf",
]
makedepends = [
    "libexif-devel",
    "lxqt-menu-data",
    "menu-cache-devel",
    "qt6-qtbase-private-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Core library of PCManFM-Qt"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/libfm-qt"
source = f"https://github.com/lxqt/libfm-qt/releases/download/{pkgver}/libfm-qt-{pkgver}.tar.xz"
sha256 = "4d8aa86fcfcf424f7f41c4a931e8d804dd12bedc8428931b5bc955345c4313a9"
hardening = ["vis", "cfi"]

@subpackage("libfm-qt-devel")
def _(self):
    return self.default_devel()
