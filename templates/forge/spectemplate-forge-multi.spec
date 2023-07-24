# This template shows how to package multiple source archives using the
# forgemeta macro.
#
# PACKAGING MULTIPLE PROJECT ARCHIVES IN A SINGLE SPEC IS DISCOURAGED. IT OFTEN
# REQUIRES ERROR-INDUCING VERSIONNING DECISIONS. In rpm, versioning is not an
# administrative decoration. Versioning controls the upgrade logic. If upstream
# deemed necessary to release a project through multiple archives, mirror its
# decision using multiple spec files. That will be safer, simpler, and
# ultimately less work.
#
# For more explanations on forgemeta, read the forgemeta-release template.
#
# Start by declaring the characteristics of each source using a	number-suffixed
# variable block:
#  – no suffix and zero suffix blocks are aliases
#  – they are “special” and identify the main source archive
#  — they use Version: to identify a release
#  – other blocks use a version<number> variable for the same need
#  – the syntax is otherwise identical to single archive mode; see the various
#    forge templates for examples.
#
# Main archive. In this example we package a full release
%global forgeurl0
Version:

# Second archive.
%global forgeurl1
%global version1

# Third archive. This time a tag. Continue as necessary.
%global forgeurl2
%global tag2

#  – use the “-a” flag to process all the source archives in a single pass
#  – use     “-z <number>” to process only the declaration block suffixed with
#    <number>
#  — without “-a” of “-z <number>” only the main archive is processed
#  – use the “-i” flag to display the variables forgemeta reads and sets
#  – use the “-v” flag if you want verbose processing
#  – remove  “-i” and “-v” before commit
%forgemeta -a

# The following lines use variables computed by forgemeta as default values.
# You can replace them with manual definitions.
# Release ordering is controlled by the packager with x%{?dist}/0.x%{?dist}
# numbers chains.
Name:
Release: 1%{?dist}
Summary:
URL:	 %{forgeurl0}
# https://github.com/rpm-software-management/rpm/issues/539
Source0: %{forgesource0}
Source1: %{forgesource1}
Source2: %{forgesource2}
%description


%prep
#  – use the “-a” flag to process all the source archives in a single pass
#  – use     “-z <number>” to process only the declaration block suffixed with
#    <number>
#  — without “-a” of “-z <number>” only the main archive is processed
#  – an autosetup wrapper, forgeautosetup, is also provided
#  – forgeautosetup does not understand “-a”
#  – use the “-v” flag if you want verbose processing; remove it before commit
#  – call forgesetup/autosetup directly if you do not like the result
%forgesetup -a
#
# After this point the archive extraction is done. forgemeta is no longer used.

%build

%install

%check

%files
%license
%doc

%changelog
