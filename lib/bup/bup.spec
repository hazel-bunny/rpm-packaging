%global forgeurl https://github.com/bup/bup
%global commit a2584f274aaae6f1428193763eed64282619fe08
%global date 20240121
%forgemeta

Name: bup
Version: 0.33.3
Release: %autorelease
Summary: Very efficient backup system based on the git packfile format

License: LGPLv2 and BSD and Python
URL:	 %{forgeurl}
Source:  %{forgesource}

BuildRequires:  gcc
BuildRequires:  sed
BuildRequires:  make
BuildRequires:  pandoc
BuildRequires:  git-core

BuildRequires:  perl-Time-HiRes
BuildRequires:  python3-devel
BuildRequires:  python3-fuse
BuildRequires:  python3-pylibacl
BuildRequires:  python3-pyxattr
BuildRequires:  python3-tornado

# For tests:
BuildRequires:  acl
BuildRequires:  attr
BuildRequires:  kmod
BuildRequires:  rsync
BuildRequires:  man-db
BuildRequires:  par2cmdline
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-xdist

Requires:       git-core
Requires:       par2cmdline
Requires:       python3
Requires:       python3-fuse
Requires:       python3-pylibacl
Requires:       python3-pyxattr
Requires:       python3-tornado


%description
%summary.


%prep
%forgeautosetup

%build
make %{?_smp_mflags} CFLAGS="${CFLAGS:-%optflags}" PYTHON=%{__python3}


%install
make install MANDIR=%{buildroot}%{_mandir} \
    DOCDIR=%{buildroot}%{_docdir}/%{name} BINDIR=%{buildroot}%{_bindir} \
    LIBDIR=%{buildroot}%{_libdir}/%{name} PYTHON=%{__python3}

# Fix hard-coded libdir location in bup's executable
sed -i 's|/lib/bup|/%{_lib}/bup|' %{buildroot}%{_bindir}/bup


#check
# Run the built-in test suite containing 3800+ tests
# (it takes < 100 seconds on a modern computer)
#make test PYTHON=%%{__python3}


%files
#doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/doc/bup
%{_libdir}/%{name}/
%{_mandir}/man1/%{name}*


%changelog
* Sun Feb 25 2024 Dipta Biswas <dabiswas112@gmail.com> 0.33.3-1
- Update to 0.33.3

* Sun May 17 2015 Tadej JaneÃ…Â¾ <tadej.j@nez.si> 0.27-0.1
- Initial package.
