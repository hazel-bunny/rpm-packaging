Name:           ladybird

%global forgeurl0 https://github.com/LadybirdBrowser/%{name}
%global commit0 bfc9dc447f42eb9d7d0927721291d1b528b3125d
%global date0 20240716

%global forgeurl1 https://github.com/microsoft/vcpkg
%global tag1 2024.08.23
%global date1 20240823

%forgemeta -a

Version:        0
Release:        1%{?dist}
Summary:        Truly independent web browser
License:        BSD
URL:            %{forgeurl0}
Source0:        %{forgesource0}
Source1:        %{forgesource1}

BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  ccache
BuildRequires:  cmake
BuildRequires:  curl
BuildRequires:  fontconfig-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  icu
BuildRequires:  libavcodec-free-devel
BuildRequires:  libavformat-free-devel
BuildRequires:  libavif-devel
BuildRequires:  liberation-sans-fonts
BuildRequires:  libglvnd-devel
BuildRequires:  libicu-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libjxl-devel
BuildRequires:  libpng-devel
BuildRequires:  libwebp-devel
BuildRequires:  nasm
BuildRequires:  ninja-build
BuildRequires:  python3-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtwayland-devel
BuildRequires:  simdutf-devel
BuildRequires:  sqlite-devel
BuildRequires:  tar
BuildRequires:  unzip
BuildRequires:  vulkan-headers
BuildRequires:  vulkan-loader-devel
BuildRequires:  woff2-devel
BuildRequires:  zip
BuildRequires:  zlib-ng-compat-static

%description
%summary

%prep
%setup -q -D -b 1 -n vcpkg-%{tag1}
%setup -q -n %{name}-%{commit0}

%build
%cmake -GNinja -Wno-dev
%ninja_build

%install
%ninja_install

install -Dm644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm644 Base/res/icons/128x128/app-browser.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%license LICENSE
