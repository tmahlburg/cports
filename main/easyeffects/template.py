pkgname = "easyeffects"
pkgver = "7.2.3"
pkgrel = 4
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gtk+3-update-icon-cache",
    "itstool",
    "meson",
    "pkgconf",
]
makedepends = [
    "appstream-glib-devel",
    "fftw-devel",
    "fmt-devel",
    "glib-devel",
    "gsl-devel",
    "gtk4-devel",
    "ladspa-sdk",
    "libadwaita-devel",
    "libbs2b-devel",
    "libebur128-devel",
    "libsamplerate-devel",
    "libsigc++-devel",
    "libsndfile-devel",
    "lilv-devel",
    "lv2",
    "nlohmann-json",
    "onetbb-devel",
    "pipewire-devel",
    "rnnoise-devel",
    "soundtouch-devel",
    "speexdsp-devel",
    "zita-convolver-devel",
]
# most plugins are from here and it can crash without them (and at least prints
# 9 million warnings), so just always pull it
depends = ["dinit-dbus", "lsp-plugins-lv2"]
pkgdesc = "PipeWire audio plugins"
license = "GPL-3.0-or-later"
url = "https://github.com/wwmm/easyeffects"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5d3afa96901c86c4fa065aa40db11800a7cdfd9d393f1de9b44bb126eee4b01e"
tool_flags = {"CXXFLAGS": ["-fexperimental-library"]}


def post_install(self):
    self.install_service("^/easyeffects.user")
