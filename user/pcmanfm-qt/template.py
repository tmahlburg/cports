pkgname = "pcmanfm-qt"
pkgver = "2.2.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "lxqt-build-tools",
    "ninja",
    "perl",
]
makedepends = [
    "layer-shell-qt-devel",
    "libexif-devel",
    "libfm-qt-devel",
    "menu-cache-devel",
    "qt6-qttools-devel",
]
pkgdesc = "File manager and desktop icon manager"
license = "GPL-2.0-or-later"
url = "https://github.com/lxqt/pcmanfm-qt"
source = f"https://github.com/lxqt/pcmanfm-qt/releases/download/{pkgver}/pcmanfm-qt-{pkgver}.tar.xz"
sha256 = "a5eeeafa8d02c9ada1b4660c238f95fde08fa13278c9ea5e191ea3bdfba1be8f"
