pkgname = "qt6-qtspeech"
pkgver = "6.9.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "qt6-qtbase-private-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtmultimedia-devel",
    "speechd-devel",
]
pkgdesc = "Qt6 Speech component"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtspeech-everywhere-src-{pkgver}.tar.xz"
sha256 = "a981b68c71743d77a3ce4437ad118d3851390f05a1ab26a859fb9b8c5938c971"
# FIXME?
hardening = ["!int"]
# cross: TODO
options = ["!cross"]


def init_check(self):
    self.make_check_env = {
        "QT_QPA_PLATFORM": "offscreen",
        "QML2_IMPORT_PATH": str(
            self.chroot_cwd / f"{self.make_dir}/lib/qt6/qml"
        ),
    }


def post_install(self):
    self.uninstall("usr/tests")


@subpackage("qt6-qtspeech-devel")
def _(self):
    self.depends += [
        f"qt6-qtbase-devel~{pkgver[:-2]}",
        f"qt6-qtdeclarative-devel~{pkgver[:-2]}",
        f"qt6-qtmultimedia-devel~{pkgver[:-2]}",
    ]
    return self.default_devel(
        extra=[
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )
