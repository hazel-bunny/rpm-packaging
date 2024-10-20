Name:           material-cursors
%global forgeurl https://github.com/varlesh/%{name}
%global commit 2a5f302fefe04678c421473bed636b4d87774b4a
%global date 20220818
%forgemeta

Version:        0
Release:        2%{?dist}
Summary:        Material Cursors
License:        GPL-2.0
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  make
BuildRequires:  git
BuildRequires:  inkscape
BuildRequires:  xcursorgen

BuildArch:      noarch

%description
%{summary}

%files
%{_datadir}/icons/material_*

#------------------------------------------------------------------

%prep
%forgeautosetup -p1

%build
%make_build

%install
%make_install

export THEMES="material_cursors material_light_cursors material_dark_cursors"
for t in $THEMES; do
    /bin/touch %{buildroot}/%{_datadir}/icons/$t/icon-theme.cache
done

%post
export THEMES="material_cursors material_light_cursors material_dark_cursors"
for t in $THEMES; do
    /bin/touch --no-create %{_datadir}/icons/$t &>/dev/null || :
done

%postun
if [ $1 -eq 0 ] ; then
    export THEMES="material_cursors material_light_cursors material_dark_cursors"
    for t in $THEMES; do
        /bin/touch --no-create %{_datadir}/icons/$t &>/dev/null
        /usr/bin/gtk-update-icon-cache %{_datadir}/icons/$t &>/dev/null || :
    done
fi

%posttrans
export THEMES="material_cursors material_light_cursors material_dark_cursors"
for t in $THEMES; do
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/$t &>/dev/null || :
done

#------------------------------------------------------------------

%changelog
* Tue Oct 15 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0-2
- Fedora 41 Mass Rebuild

* Sun Apr 28 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0-1.git
- initial package
