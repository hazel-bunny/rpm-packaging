%global __cargo_skip_build 0

Name:           newsflash
Version:        1.5.1
Release:        %autorelease
Summary:        Modern feed reader

# 0BSD or MIT or ASL 2.0
# ASL 2.0
# ASL 2.0 or Boost
# ASL 2.0 or MIT
# ASL 2.0 or MIT or MPLv2.0
# BSD
# GPLv3+
# LGPLv2
# MIT
# MIT or ASL 2.0
# MIT or ASL 2.0 or zlib
# MIT or zlib or ASL 2.0
# Unlicense
# Unlicense or MIT
# zlib
# zlib or ASL 2.0 or MIT
License:        GPLv3+ and BSD and ASL 2.0 and MIT and Unlicense and zlib
URL:            https://gitlab.com/news-flash/news_flash_gtk
Source0:        %{url}/-/archive/%{version}/news_flash_gtk-%{version}.tar.bz2

# * convert news-flash dependency from git reference to published version
Patch0:         newsflash-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%description
A modern feed reader designed for the GNOME desktop. NewsFlash is a program
designed to complement an already existing web-based RSS reader account.

It combines all the advantages of web based services like syncing across all
your devices with everything you expect from a modern desktop program:
Desktop notifications, fast search and filtering, tagging, handy keyboard
shortcuts and having access to all your articles as long as you like.

%prep
%autosetup -n news_flash_gtk-%{version} -p1
# We will build by cargo ourselves
sed -i -e '/\(build_by_default\|install\)/s/true/false/' src/meson.build
sed -i -e '/dependency/d' meson.build
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo 'meson'
echo '/usr/bin/appstream-util'
echo '/usr/bin/desktop-file-validate'

%build
%meson
%meson_build
export FEEDLY_CLIENT_ID="boutroue"
export FEEDLY_CLIENT_SECRET="FE012EGICU4ZOBDRBEOVAJA1JZYH"
export PASSWORD_CRYPT_KEY="ypsSXCLhJngks9qGUAqShd8JjRaZ824wT3e"
%cargo_build

%install
%meson_install
%cargo_install
mv %{buildroot}%{_bindir}/{news_flash_gtk,com.gitlab.newsflash}
# clean up buildroot pollution caused by build system errors
rm -rf %{buildroot}/builddir

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/com.gitlab.newsflash.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/com.gitlab.newsflash.appdata.xml

%files
%license LICENSE
%doc README.md
%{_bindir}/com.gitlab.newsflash
%{_datadir}/applications/com.gitlab.newsflash.desktop
%{_datadir}/icons/hicolor/*/apps/com.gitlab.newsflash*
%{_datadir}/metainfo/com.gitlab.newsflash.appdata.xml

%changelog
%autochangelog
