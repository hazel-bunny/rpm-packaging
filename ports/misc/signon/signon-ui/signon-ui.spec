%global forgeurl https://gitlab.com/accounts-sso/signon-ui
%global commit 4368bb77d9d1abc2978af514225ba4a42c29a646
%global date 20171022
%forgemeta

Name:           signon-ui
Version:        0.17+15.10.20150810
Release:        %autorelease
Summary:        Online Accounts Sign-on UI
License:        GPLv3
URL:            %{forgeurl}

Source0:        %{forgesource}
Patch0:         fake-user-agent.patch

BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  libaccounts-qt5-devel
BuildRequires:  signon-devel
BuildRequires:  libproxy-devel
BuildRequires:  libnotify-devel
BuildRequires:  qt5-qtwebengine-devel
BuildRequires:  qt5-rpm-macros

Requires:       dbus

%description
Sign-on UI is the component responsible for handling the user interactions which
can happen during the login process of an online account.
It can show password dialogs and dialogs with embedded web pages.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files
%doc README TODO NOTES
%license COPYING
%{_bindir}/signon-ui
%{_datadir}/applications/signon-ui.desktop
%{_datadir}/dbus-1/services/*.service
%{_sysconfdir}/signon-ui

%prep
%forgeautosetup -p1
# Do not install tests
sed -e 's|src \\|src|' -e '/tests/d' -i signon-ui.pro

%build
export PATH=%{_qt5_bindir}:$PATH
%{qmake_qt5} QMF_INSTALL_ROOT=%{_prefix} CONFIG+=release signon-ui.pro
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}
# Own directory where others can install provider-specific configuration
mkdir -p %{buildroot}/%{_sysconfdir}/signon-ui/webkit-options.d

%changelog
%autochangelog
