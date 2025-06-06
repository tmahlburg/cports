pkgname = "perl-authen-sasl"
pkgver = "2.1800"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl", "perl-digest-hmac"]
depends = ["perl", "perl-digest-hmac"]
pkgdesc = "SASL authentication framework"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/Authen-SASL"
source = f"$(CPAN_SITE)/Authen/Authen-SASL-{pkgver}.tar.gz"
sha256 = "0b03686bddbbf7d5c6548e468d079a4051c9b73851df740ae28cfd2db234e922"
