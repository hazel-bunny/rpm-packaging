%global app_id com.linuxmint.mintstick

Name:           mintstick
Version:        1.5.6
Release:        3%{?dist}
Group:          Applications/System
License:        GPL
URL:            https://github.com/linuxmint/%{name}
Summary:        Format USB sticks and create bootable USB sticks

Source:         https://mirror.0x.sg/linuxmint/pool/main/m/%{name}/%{name}_%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  python3-devel

Requires:       coreutils
Requires:       desktop-file-utils
Requires:       dosfstools
Requires:       e2fsprogs
Requires:       exfatprogs
Requires:       glib2
Requires:       gtk3
Requires:       libunity
Requires:       ntfs-3g
Requires:       parted
Requires:       polkit
Requires:       procps-ng
Requires:       python3
Requires:       python3-dbus
Requires:       python3-gobject
Requires:       python3-pyparted
Requires:       python3-xapp
Requires:       udisks2
Requires:       util-linux
Requires:       xapps

%description
Mintstick is a graphical tool that allows you to format USB sticks and create bootable USB sticks.

%prep
%setup -q -n %{name}
sed -i 's,/usr/lib/,%{_libdir}/,' %{name}

%build
%py_byte_compile %{python3} lib/*.py

%install
LIBFILES="%{name}.py raw_write.py raw_format.py mountutils.py verify.py"

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_datadir}/polkit-1/actions
mkdir -p %{buildroot}%{_datadir}/kde4/apps/solid/actions

cp %{name} %{buildroot}%{_bindir}/
cp mint-iso-verify %{buildroot}%{_bindir}/

cp -r share/applications %{buildroot}%{_datadir}
cp -r share/icons %{buildroot}%{_datadir}
cp -r share/%{name} %{buildroot}%{_datadir}
cp -r share/nemo %{buildroot}%{_datadir}
cp share/polkit/%{app_id}.policy %{buildroot}%{_datadir}/polkit-1/actions/
cp share/kde4/%{name}-format_action.desktop %{buildroot}%{_datadir}/kde4/apps/solid/actions/

for item in $LIBFILES; do
    cp lib/$item %{buildroot}%{_libdir}/%{name}/
done

%files
%doc README.md COPYING
%{_bindir}/%{name}
%{_bindir}/mint-iso-verify
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_datadir}/icons/hicolor/scalable/status/%{name}*
%{_datadir}/kde4/apps/solid/actions/%{name}-format_action.desktop
%{_datadir}/nemo/actions/%{name}*.nemo_action
%{_datadir}/polkit-1/actions/%{app_id}.policy

%changelog
* Wed Jul 5 2023 Dipta Biswas <dabiswas112@gmail.com> 1.5.6-3
- Fix binary

* Wed Jul 5 2023 Dipta Biswas <dabiswas112@gmail.com> 1.5.6-2
- Update dependencies and files

* Wed Jul 5 2023 Dipta Biswas <dabiswas112@gmail.com> 1.5.6-1
- Import from alanfla/mintstick
- Refactor spec

* Fri Nov 13 2020 builder
- Build initial package rpm.
