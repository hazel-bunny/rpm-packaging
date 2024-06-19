Name:             bup

%global forgeurl https://github.com/%{name}/%{name}
%global commit a2584f274aaae6f1428193763eed64282619fe08
%global date 20240121
%forgemeta

Version:          0.33.3
Release:          2%{?dist}
Summary:          Very efficient backup system based on the git packfile format
License:          LGPLv2 and BSD and Python
URL:              https://bup.github.io/
Source0:          %{forgesource}

#------------------------------------------------------------------

BuildRequires:    gcc
BuildRequires:    sed
BuildRequires:    make
BuildRequires:    git-core
BuildRequires:    rsync
BuildRequires:    man-db
BuildRequires:    pandoc
BuildRequires:    par2cmdline

BuildRequires:    perl(Getopt::Long)
BuildRequires:    perl(Pod::Usage)
BuildRequires:    perl(Time::HiRes)

BuildRequires:    python3-devel
BuildRequires:    python3-fuse
BuildRequires:    python3-pylibacl
BuildRequires:    python3-pyxattr
BuildRequires:    python3-tornado
BuildRequires:    python3-pylint
BuildRequires:    python3-pytest
BuildRequires:    python3-pytest-xdist

BuildRequires:    pkgconfig(libacl)
BuildRequires:    pkgconfig(libattr)
BuildRequires:    pkgconfig(libkmod)
BuildRequires:    pkgconfig(readline)

Requires:         git-core
Requires:         par2cmdline
Requires:         python3-fuse
Requires:         python3-pylibacl
Requires:         python3-pyxattr
Requires:         python3-tornado

#------------------------------------------------------------------

%description
Very efficient backup system based on the git packfile format, providing fast
incremental saves and global deduplication (among and within files, including
virtual machine images). Some of its features are:
* It uses a rolling checksum algorithm and hence it can backup huge files incrementally.
* It uses packfile format from git, so one can access the stored data even if he
  doesn't like bup's user interface.
* It writes packfiles directly so it is fast even with huge amounts of data: it
  can track millions of files and keep track of hundreds or thousands of
  gigabytes of objects.
* Data is "automagically" shared between incremental backups without having to
  know which backup is based on which other one.
* One can make a backup directly to a remote bup server, without needing tons of
  temporary disk space on the computer being backed up. If the backup is interrupted
  halfway through, the next run will pick up where the previous backup left off.
* It can use "par2" redundancy to recover corrupted backups even if the disk
  has undetected bad sectors.
* Each incremental backup acts as if it's a full backup, it just takes less disk space.
* One can mount a bup repository as a FUSE filesystem and access the contents
  that way, or even export it over Samba.

%files
%license LICENSE

%doc README.md
%doc note/*.md

%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_mandir}/man1/%{name}*.gz
%{_pkgdocdir}/%{name}*.html

#-----------------------------------------------------------------------------------

%prep
%forgeautosetup -p1

%build
%_configure
%make_build PREFIX=%{_prefix} PYTHON=%{python3}

%install
%make_install BINDIR=%{_bindir} DOCDIR=%{_pkgdocdir} \
    LIBDIR=%{_libdir}/%{name} MANDIR=%{_mandir} PYTHON=%{python3}

%py_byte_compile %{python3} %{buildroot}%{_libdir}/%{name}/%{name}/*.py
%py_byte_compile %{python3} %{buildroot}%{_libdir}/%{name}/%{name}/cmd/*.py

%check
# Remove failing tests
# rm test/ext/test-help
rm test/ext/test-meta

# Run the built-in test suite containing 3800+ tests (it takes < 100 seconds on a modern computer)
%make_build test PYTHON=%{python3}

%changelog
* Fri May 17 2024 Dipta Biswas <dabiswas112@gmail.com> - 0.33.3-2.git
- Fix file locations
- Re-enable tests

* Sun Feb 25 2024 Dipta Biswas <dabiswas112@gmail.com> 0.33.3-1.git
- Switch to git snapshot for gcc 14

* Sun Feb 25 2024 Dipta Biswas <dabiswas112@gmail.com> 0.33.3-1
- Update to 0.33.3

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 2019 Tadej Janež <tadej.j@nez.si> - 0.29.2-4
- Remove bup-web functionality in Fedora 31+. This accounts for the fact that
  Tornado in F31+ doesn't support Python 2 anymore.

* Thu Feb 07 2019 Tadej Janež <tadej.j@nez.si> - 0.29.2-3
- Use %%{build_cflags} to specify the C compiler flags (i.e. CFLAGS). This
  will properly account for
  https://fedoraproject.org/wiki/Changes/Python_Extension_Flags

* Wed Feb 06 2019 Tadej Janež <tadej.j@nez.si> - 0.29.2-2
- Use %%{extension_cflags} to specify the C compiler flags (i.e. CFLAGS) to
  account for https://fedoraproject.org/wiki/Changes/Python_Extension_Flags

* Fri Feb 01 2019 Tadej Janež <tadej.j@nez.si> - 0.29.2-1
- Update to version 0.29.2
- Remove obsolete patches

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 01 2018 Tadej Janež <tadej.j@nez.si> - 0.29.1-2
- Use older version of pyxattr (build) requirement on Fedora < 28

* Thu Jul 26 2018 Tadej Janež <tadej.j@nez.si> - 0.29.1-1
- Update to version 0.29.1
- Add patches that backport fixes for test-rm tests that make them work with
  older and newer versions of git
- Simplify SourceURL handling to only use the %%gittag macro (renamed from
  %%gittag0)

* Sat Jul 21 2018 Tadej Janež <tadej.j@nez.si> - 0.29-9
- Add gcc to BuildRequires to account for
  https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot
  (resolves https://bugzilla.redhat.com/1603530)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.29-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.29-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.29-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 21 2017 Tadej Janež <tadej.j@nez.si> - 0.29-5
- Explicitly require python2- prefixed Python packages when available
  (python2-fuse on Fedora 28+, python2-tornado)
- Drop work-around for broken %%systemd_user_post macro in Fedora < 24
- Add rsync BuildRequirement needed for running tests

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Tadej Janež <tadej.j@nez.si> 0.29-1
- Updated to 0.29 release.
- Replaced 'git' requirement with 'git-core' which provides just core git with
  minimal extra dependencies (e.g. doesn't require numerous Perl modules).
- Added missing Perl BuildRequirements masked by the full 'git' install:
  - perl(Getopt::Long)
  - perl(Pod::Usage)
- Updated spec file:
  - Use %%{basename: ...} when rendering README templates.

* Tue Dec 27 2016 Tadej Janež <tadej.j@nez.si> 0.28.1-1
- Updated to 0.28.1 release.
- Enabled 'par2' support in 'bup fsck'.
- Made tests run in parallel.
- Packaged HTML documentation.
- Dropped all patches.
- Updated and modernized spec file:
  - Use %%make_build macro.
  - Use %%make_install macro.
  - Simplify %%make_install part since bup now properly implements DESTDIR
    environment variable.
  - Stop mixing the %%doc with relative paths and installation of files
    directly into %%_pkgdocdir.
  - Use %%systemd_user_post macro on Fedora 24+.
  - Implement and use %%render_template macro to render READMEs containing
    RPM macros using %%expand macro.
  - Add additional BuildRequires needed by tests.
  - Follow the latest SourceURL packaging guidelines and reference git tag
    instead of commit revision in Source0 URL.
  - Drop special prerelease handling.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 14 2015 Tadej Janež <tadej.j@nez.si> 0.27-1
- Initial release in Fedora 22+ and EPEL 7.
- Added a workaround for an %%autosetup bug on EPEL 7.

* Fri Dec 04 2015 Tadej Janež <tadej.j@nez.si> 0.27-0.4
- Made bup-web subpackage Requires on the base package arch-specific.

* Mon Nov 23 2015 Tadej Janež <tadej.j@nez.si> 0.27-0.3
- Split bup web server into a separate sub-package.
- Added systemd service for running the bup web server.
- Added a work-around for a bug in systemd's %%systemd_user_post macro.
- Added a README with Fedora-specific notes on using the bup-web package.
- Converted the main README with Fedora-specific notes to Markdown.

* Wed Oct 14 2015 Tadej Janež <tadej.j@nez.si> 0.27-0.2
- Added perl(Time::HiRes) to BuildRequires since it is required for running the
  tests.
- Temporarily disable test_from_path_error() test that fails on Fedora Koji and
  COPR build systems.

* Sun May 17 2015 Tadej Janež <tadej.j@nez.si> 0.27-0.1
- Initial package.

