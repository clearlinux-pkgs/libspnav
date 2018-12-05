#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libspnav
Version  : 0.2.3
Release  : 6
URL      : https://github.com/FreeSpacenav/libspnav/releases/download/libspnav-0.2.3/libspnav-0.2.3.tar.gz
Source0  : https://github.com/FreeSpacenav/libspnav/releases/download/libspnav-0.2.3/libspnav-0.2.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: libspnav-lib = %{version}-%{release}
BuildRequires : pkgconfig(x11)
Patch1: build.patch

%description
libspnav - 0.2.3
----------------
1. About
The libspnav library is provided as a replacement of the magellan library. It
provides a cleaner, and more orthogonal interface. libspnav supports both the
original X11 protocol for communicating with the driver, and the new
alternative non-X protocol. Programs that choose to use the X11 protocol, are
automatically compatible with either the free spacenavd driver or the official
3dxserv, as if they were using the magellan SDK.

%package dev
Summary: dev components for the libspnav package.
Group: Development
Requires: libspnav-lib = %{version}-%{release}
Provides: libspnav-devel = %{version}-%{release}

%description dev
dev components for the libspnav package.


%package lib
Summary: lib components for the libspnav package.
Group: Libraries

%description lib
lib components for the libspnav package.


%prep
%setup -q -n libspnav-0.2.3
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1544000397
%configure --disable-static libdir=lib64
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1544000397
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libspnav.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libspnav.so.0
/usr/lib64/libspnav.so.0.1
