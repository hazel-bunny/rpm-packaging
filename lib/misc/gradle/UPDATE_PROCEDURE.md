Gradle update procedure is not trivial, due to large number of
patches, frequent API/ABI breaks and cyclic build-dependency between
Gradle and XMvn.  This document tries to help maintainers by
describing steps that are necessary for updating Gradle to new
upstream version.


Preparing XMvn Connector for Gradle
===================================

You yould always start with porting XMvn to use given Gradle version.

Patches to XMvn can be submitted as pull requests on Github, where XMvn is hosted:
https://github.com/fedora-java/xmvn

Upload Gradle binaries to XMvn remote repo
------------------------------------------

This is done by running the following command from XMvn upstream git
directory:

    ./aux/deploy-gradle.sh 2.5-rc-1

Port XMvn to given Gradle version
---------------------------------

First you need to adjust `<gradleVersion>` in `xmvn-parent/pom.xml`:

    v=2.5-rc-2
    sed -i "/<gradleVersion>/s/>.*</>$v</" xmvn-parent/pom.xml
    git commit -a -m "Port to gradle $v"

Then see if it builds and all tests pass:

    mvn clean verify

If not, fix build problems and amend commit:

    git commit -a --amend -C HEAD

Backport XMvn patch
-------------------

If there were any code changes required (POM version bump doesn't
count) then you'll need to backport the patch to latest XMvn version
that is in rawhide.  Simply use git to rebase the commit on top of
latest release and prepare patch from it.


Preparing Gradle update
=======================

First, regenerate bootstrap resources:

    v=2.5-rc-2
    wget http://services.gradle.org/distributions/gradle-${v}-bin.zip
    unzip gradle-${v}-bin.zip
    ./gradle-bootstrap-gererate-resources.py gradle-${v}
    git commit -a -m "Regenerate bootstrap resources"

Then rebase patches on top of upstream release.

Lastly, bump spec file and try building the package.


Bootstrapping Gradle
====================

This is only necessary if Gradle broke its API or it broke XMvn
(i.e. there were code changes required when porting XMvn), otherwise
it can be skipped.  In any case it is recommended to do this step at
least as scratch build in order to make sure that bootstrap procedure
is still working.

First step of bootstrap procedure is doing bootstrap build.  For this
you need to change `%bcond_with bootstrap` to `%bcond_without
bootstrap` in spec file and build the package.

Secondly, if there is XMvn patch to be applied, you should do it now
and build `xmvn` package.

Finally, revert `%bcond` to its initial (non-bootstrap) state and do
final non-bootstrap build of `gradle`.
