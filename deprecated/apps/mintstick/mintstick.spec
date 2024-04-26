%global forgeurl https://github.com/linuxmint/mintstick
%global commit 750c6bb8b41dd70630bb7790643407acd7992378
%global date 20230328
%forgemeta

%global app_id com.linuxmint.mintstick

Name:           mintstick
Version:        1.5.6
Release:        %autorelease
Epoch:          1
Group:          Applications/System
License:        GPL
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils

Requires:       coreutils
Requires:       dosfstools
Requires:       e2fsprogs
Requires:       exfatprogs
Requires:       glib2
Requires:       gtk3
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

Recommends:     libunity
Recommends:     python3-libunity
Recommends:     (nemo-extension-%{name} if nemo)

%description
Mintstick is a graphical tool that allows you to format USB sticks and create bootable USB sticks.

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
%{_datadir}/polkit-1/actions/%{app_id}.policy

#------------------------------------------------------------------

%package -n nemo-extension-%{name}
Summary:        Integration of Mintstick with Nemo file manager
Group:          Graphical desktop/Cinnamon
Requires:       nemo

%description -n nemo-extension-%{name}
Integration of Mintstick with Nemo file manager

%files -n nemo-extension-%{name}
%{_datadir}/nemo/actions/%{name}*.nemo_action

#------------------------------------------------------------------

%prep
%forgeautosetup -p1
sed -i 's,/usr/lib/,%{_libdir}/,' %{name}

%build
#nothing

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_datadir}/polkit-1/actions
mkdir -p %{buildroot}%{_datadir}/kde4/apps/solid/actions

install -Dm 755 %{name} -t %{buildroot}%{_bindir}
install -Dm 755 mint-iso-verify -t %{buildroot}%{_bindir}

cp lib/* %{buildroot}%{_libdir}/%{name}/
cp -r share/applications %{buildroot}%{_datadir}/
cp -r share/icons %{buildroot}%{_datadir}/
cp -r share/%{name} %{buildroot}%{_datadir}/
cp -r share/nemo %{buildroot}%{_datadir}/
cp share/polkit/%{app_id}.policy %{buildroot}%{_datadir}/polkit-1/actions/
cp share/kde4/%{name}-format_action.desktop %{buildroot}%{_datadir}/kde4/apps/solid/actions/

%py_byte_compile %{python3} %{buildroot}%{_libdir}/%{name}/*.py

#------------------------------------------------------------------

%changelog
%autochangelog
