%global toolchain clang

%if 0%{?fedora} > 40
%global _lto_cflags %nil
%endif

%global gitdate 20241017
%global gitcommit_full f0add9c08c0f6a21e6493a22235458a5329d9101
%global gitcommit %%(c=%%{gitcommit_full}; echo ${c:0:7})

Name:           kio-onedrive
Version:        0.0.3^%{gitdate}.%{gitcommit}
Release:        1%{?dist}
Summary:        KIO worker to access OneDrive

License:        GPL-2.0-or-later
URL:            https://invent.kde.org/bernardogn/%{name}
Source0:        https://invent.kde.org/bernardogn/%{name}/-/archive/%{gitcommit_full}/%{name}-%{gitcommit_full}.tar.bz2

BuildRequires:  cmake
BuildRequires:  clang
BuildRequires:  clang-tools-extra
BuildRequires:  compiler-rt
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KAccounts6)

# BuildRequires:  gettext
# BuildRequires:  libappstream-glib
# BuildRequires:  cmake(KF6Parts)
# BuildRequires:  cmake(KF6IconThemes)
# BuildRequires:  cmake(KF6DocTools)
# BuildRequires:  cmake(KF6Crash)
# BuildRequires:  cmake(KF6CoreAddons)
# BuildRequires:  cmake(KF6Bookmarks)
# BuildRequires:  qt6-qt5compat-devel
# BuildRequires:  boost-devel

%description
%summary


%prep
%autosetup -p1 -n %{name}-%{gitcommit_full}

%build
%cmake_kf6 -GNinja -DCMAKE_CXX_COMPILER_CLANG_SCAN_DEPS:FILEPATH=/usr/bin/clang-scan-deps
%ninja_build -C %{_vpath_builddir}

%install
%ninja_install -C %{_vpath_builddir}

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/remoteview/onedrive.desktop

%files
%license LICENSES/*
%doc README.md
%{_kf6_plugindir}/kio/DriveItem.pcm
%{_kf6_plugindir}/kio/OnedriveWorker.pcm
%{_kf6_plugindir}/kio/URLHandler.pcm
%{_kf6_plugindir}/kio/URLUtils.pcm
%{_kf6_plugindir}/kio/onedrive.so
%{_kf6_datadir}/accounts/providers/kde/microsoft.provider
%{_kf6_datadir}/accounts/services/kde/microsoft-onedrive.service
%{_kf6_datadir}/remoteview/onedrive.desktop

%changelog
* Thu Oct 17 2024 Hazel Bunny <hazel_bunny@disroot.org> - 0.0.3^20241017.f0add9c0-1
- Initial package

