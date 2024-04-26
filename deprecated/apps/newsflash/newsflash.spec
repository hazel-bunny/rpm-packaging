%global app_id com.gitlab.newsflash
%global forgeurl https://gitlab.com/news-flash/news_flash_gtk
%global tag 2.3.0
%forgemeta

%global __cargo_skip_build 0

Name:           newsflash
Version:        %{tag}
Release:        %autorelease
Summary:        Follow your favorite blogs & news sites

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
URL:            %{forgeurl}
Source:         %{forgesource}

# * convert news-flash dependency from git reference to published version
# Patch0:         newsflash-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%description
NewsFlash is a program designed to complement an already existing web-based RSS
reader account. It combines all the advantages of web based services like syncing
across all your devices with everything you expect from a modern desktop program:
Desktop notifications, fast search and filtering, tagging, handy keyboard shortcuts
and having access to all your articles as long as you like.

%prep
%forgeautosetup -n news_flash_gtk-%{version} -p1
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
mv %{buildroot}%{_bindir}/{news_flash_gtk,%{app_id}}
# clean up buildroot pollution caused by build system errors
rm -rf %{buildroot}/builddir

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{app_id}.appdata.xml

%files
%license LICENSE
%doc README.md
%{_bindir}/%{app_id}
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/icons/hicolor/*/apps/%{app_id}*
%{_metainfodir}/%{app_id}.appdata.xml

%changelog
%autochangelog
