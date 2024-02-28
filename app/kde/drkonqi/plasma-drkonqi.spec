%global base_name drkonqi

Name:    plasma-drkonqi
Summary: DrKonqi crash handler for KF6/Plasma6
Version: 6.0.0
Release: %autorelease
Epoch:   1

License: GPLv2+
URL:     https://invent.kde.org/plasma/%{base_name}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        https://download.kde.org/%{stable}/plasma/%{version}/%{base_name}-%{version}.tar.xz

## upstreamable Patches
# dnf debuginfo-install
Patch52:        drkonqi-installdbgsymbols.patch

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  desktop-file-utils

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Quick)
 
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  cmake(PolkitQt6-1)

BuildRequires:  systemd-devel
BuildRequires:  git-core
 
Requires:       kf6-kirigami
Requires:       kf6-kitemmodels
Requires:       kf6-kcmutils
Requires:       konsole
Requires:       polkit
Requires:       (dnf-command(debuginfo-install) if dnf)
Requires:       python3-psutil
Requires:       python3-pygdbmi
Requires:       python3-sentry-sdk
Requires:       systemd-udev

# retired from plasma-workspace
Obsoletes: plasma-workspace-drkonqi < 5.10.95
Provides: plasma-workspace-drkonqi = %{version}-%{release}

%description
%{summary}

%prep
%autosetup -n %{base_name}-%{version} -p1

%build
%cmake_kf6 -DWITH_PYTHON_VENDORING=OFF -DWITH_GDB12=TRUE
%cmake_build

%install
%cmake_install
# installdbgsymbols script
install -p -D -m755 src/doc/examples/installdbgsymbols_fedora.sh \
    %{buildroot}%{_libexecdir}/installdbgsymbols.sh

%find_lang all --with-html --with-qt --all-name
grep drkonqi.mo all.lang > plasma-drkonqi.lang

%post
%systemd_user_post drkonqi-sentry-postman.service

%preun
%systemd_user_preun drkonqi-sentry-postman.service

%postun
%systemd_user_postun drkonqi-sentry-postman.service

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.{drkonqi.coredump.gui,drkonqi}.desktop

%files -f plasma-drkonqi.lang
%license LICENSES/*
%{_bindir}/drkonqi-coredump-gui
%{_libexecdir}/drkonqi
%{_libexecdir}/installdbgsymbols.sh
%{_libexecdir}/drkonqi-coredump-cleanup
%{_libexecdir}/drkonqi-coredump-launcher
%{_libexecdir}/drkonqi-coredump-processor
%{_kf6_datadir}/drkonqi/
%{_kf6_datadir}/applications/org.kde.drkonqi.coredump.gui.desktop
%{_kf6_datadir}/applications/org.kde.drkonqi.desktop
%{_kf6_datadir}/qlogging-categories6/drkonqi.categories
%{_userunitdir}/drkonqi-coredump-*
%{_unitdir}/drkonqi-coredump-processor@.service
%{_qt6_plugindir}/drkonqi/KDECoredumpNotifierTruck.so
%{_bindir}/drkonqi-sentry-data
%{_unitdir}/systemd-coredump@.service.wants/drkonqi-coredump-processor@.service
%{_userunitdir}/default.target.wants/*
%{_userunitdir}/drkonqi-sentry-postman.*
%{_userunitdir}/plasma-core.target.wants/drkonqi-*
%{_userunitdir}/sockets.target.wants/drkonqi-coredump-launcher.socket
%{_userunitdir}/timers.target.wants/drkonqi-*
%{_libexecdir}/drkonqi-sentry-postman
%{_kf6_libexecdir}/drkonqi-polkit-helper
%{_kf6_datadir}/dbus-1/system-services/org.kde.drkonqi.service
%{_kf6_datadir}/dbus-1/system.d/org.kde.drkonqi.conf
%{_kf6_datadir}/polkit-1/actions/org.kde.drkonqi.policy

%changelog
%autochangelog
