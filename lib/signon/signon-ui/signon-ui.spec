Name:           signon-ui
Version:        0.17+15.10.20150810
Release:        %autorelease
Summary:        Online Accounts Sign-on Ui

License:        GPLv3
URL:            https://gitlab.com/accounts-sso/signon-ui

Source0:        https://gitlab.com/accounts-sso/signon-ui/-/archive/%{version}-0ubuntu1/signon-ui-%{version}-0ubuntu1.tar.gz

BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtwebkit-devel
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


%prep
%setup -q -n signon-ui-%{version}-0ubuntu1


%build
export PATH=%{_qt5_bindir}:$PATH
%{qmake_qt5} QMF_INSTALL_ROOT=%{_prefix} \
    CONFIG+=release signon-ui.pro

make %{?_smp_mflags}


%install
make install INSTALL_ROOT=%{buildroot}

# Own directory where others can install provider-specific configuration
mkdir -p %{buildroot}/%{_sysconfdir}/signon-ui/webkit-options.d

%files
%doc README TODO NOTES
%license COPYING
%{_bindir}/signon-ui
%{_datadir}/dbus-1/services/*.service
%{_sysconfdir}/signon-ui

%changelog
%autochangelog
