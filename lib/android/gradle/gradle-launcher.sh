#!/usr/bin/bash

set -e
ulimit -n $(ulimit -H -n)

# Source system prefs
if [ -f /etc/java/gradle.conf ] ; then
  . /etc/java/gradle.conf
fi

# Source user prefs
if [ -f $HOME/.gradlerc ] ; then
  . $HOME/.gradlerc
fi

. /usr/share/java-utils/java-functions
set_jvm
set_javacmd

set_classpath gradle/gradle-launcher gradle/gradle-core-api gradle/gradle-core gradle/gradle-base-services

# Split up the JVM_OPTS And GRADLE_OPTS values into an array, following the shell quoting and substitution rules
function splitJvmOpts() {
    JVM_OPTS=("$@")
}
eval splitJvmOpts $JAVA_OPTS $GRADLE_OPTS
JVM_OPTS[${#JVM_OPTS[*]}]="-Dorg.gradle.appname=gradle"

exec "$JAVACMD" "${JVM_OPTS[@]}" -classpath "$CLASSPATH" org.gradle.launcher.GradleMain "$@"
