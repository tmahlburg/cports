pkgname = "gnome-control-center"
pkgver = "48.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "libxml2-progs",
    "meson",
    "pkgconf",
    "polkit",
    "python",
    "tecla",
]
makedepends = [
    "accountsservice-devel",
    "colord-devel",
    "colord-gtk-devel",
    "cups-devel",
    "gcr-devel",
    "glib-devel",
    "gnome-bluetooth-devel",
    "gnome-desktop-devel",
    "gnome-online-accounts-devel",
    "gnome-settings-daemon-devel",
    "gnutls-devel",
    "gsettings-desktop-schemas-devel",
    "gsound-devel",
    "gtk4-devel",
    "heimdal-devel",
    "ibus-devel",
    "libepoxy-devel",
    "libgtop-devel",
    "libgudev-devel",
    "libhandy-devel",
    "libnma-devel",
    "libpulse-devel",
    "libpwquality-devel",
    "libsecret-devel",
    "libsoup-devel",
    "libwacom-devel",
    "libx11-devel",
    "libxi-devel",
    "libxml2-devel",
    "modemmanager-devel",
    "networkmanager-devel",
    "polkit-devel",
    "samba-client-devel",
    "udisks-devel",
    "upower-devel",
]
depends = [
    "cups-pk-helper",
    "desktop-file-utils",
    "fprintd-meta",
    "gsettings-desktop-schemas",
    "power-profiles-daemon-meta",
    "sound-theme-freedesktop",
    "system-config-printer",
    "tecla",
    "udisks",
]
checkdepends = ["python-dbusmock", "xwayland-run", *depends]
pkgdesc = "GNOME control center"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-control-center"
source = f"$(GNOME_SITE)/gnome-control-center/{pkgver.split('.')[0]}/gnome-control-center-{pkgver}.tar.xz"
sha256 = "d2ec4a5e27e191d92f98ed4dbc4a861d7f1ac4a5a24b6524b492a12007dd460c"


@subpackage("gnome-control-center-devel")
def _(self):
    self.depends += [self.parent]

    return self.default_devel()
