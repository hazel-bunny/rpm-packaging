%undefine __cmake_in_source_build

%global base_name    drkonqi

Name:    plasma-drkonqi
Summary: DrKonqi crash handler for KF5/Plasma5
Version: 5.27.7
Release: %autorelease
Epoch:   1

License: GPLv2+
URL:     https://cgit.kde.org/%{base_name}.git

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

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  systemd-rpm-macros

BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5XmlRpcClient)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5IdleTime)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(KUserFeedback)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  systemd-devel

# retired from plasma-workspace
Obsoletes: plasma-workspace-drkonqi < 5.10.95
Provides: plasma-workspace-drkonqi = %{version}-%{release}

Requires: (dnf-command(debuginfo-install) if dnf)
Requires: konsole5
Requires: polkit
# owner of setsebool
Requires(post): policycoreutils

%description
%{summary}


%prep
%setup -q -n %{base_name}-%{version}

%patch -P 52 -p1 -b .installdgbsymbols

%build
%cmake_kf5 -DWITH_GDB12=TRUE
%cmake_build

%install
%cmake_install
# installdbgsymbols script
install -p -D -m755 src/doc/examples/installdbgsymbols_fedora.sh \
    %{buildroot}%{_libexecdir}/installdbgsymbols.sh

%find_lang all --with-html --with-qt --all-name
grep drkonqi5.mo all.lang > plasma-drkonqi.lang

%post
# make DrKonqi work by default by taming SELinux enough (suggested by dwalsh)
# if KDE_DEBUG is set, DrKonqi is disabled, so do nothing
# if it is unset (or empty), check if deny_ptrace is already disabled
# if not, disable it
if [ -z "$KDE_DEBUG" ] ; then
if [ "`getsebool deny_ptrace 2>/dev/null`" == 'deny_ptrace --> on' ] ; then
  setsebool -P deny_ptrace off &> /dev/null || :
fi
fi

%files -f plasma-drkonqi.lang
%license LICENSES/*
%{_bindir}/drkonqi-coredump-gui
%{_libexecdir}/drkonqi
%{_libexecdir}/installdbgsymbols.sh
%{_libexecdir}/drkonqi-coredump-cleanup
%{_libexecdir}/drkonqi-coredump-launcher
%{_libexecdir}/drkonqi-coredump-processor
%{_kf5_datadir}/drkonqi/
%{_kf5_datadir}/applications/org.kde.*.desktop
%{_kf5_datadir}/qlogging-categories5/drkonqi.categories
%{_userunitdir}/drkonqi-coredump-*
%{_unitdir}/drkonqi-coredump-processor@.service
%{_qt5_plugindir}/drkonqi/KDECoredumpNotifierTruck.so

%changelog
%autochangelog
