%define git 1

%global _basename hamster

%global commit 15db58b0c85663f2d3d43a531c0f865234e5f9bf
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20230615