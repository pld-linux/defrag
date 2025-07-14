#
# Conditional build:
%bcond_without	static		# don't build static
#
Summary:	Linux filesystem defragmenter
Summary(pl.UTF-8):	Narzędzia do defragmentacji linuksowych systemów plików
Name:		defrag
Version:	0.73
Release:	2
License:	GPL
Group:		Applications/System
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/filesystems/%{name}-%{version}.tar.gz
# Source0-md5:	d007c46b3cbd7de495deb45a50836d18
Patch0:		%{name}-0.73-glibc.patch
Patch1:		%{name}-makefile.patch
Patch2:		%{name}-kernel-2.4.patch
Patch3:		%{name}-shared.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux filesystem defragmenters. The programs in this package will
reorganise data on minix, ext, ext2 and xia file system partitions in
order to improve the file system's performance.

%description -l pl.UTF-8
Programy do defragmentacji systemu plików Linuksa. Zawarte w tym
pakiecie programy mają za zadanie reorganizację danych na partycjach
minix, ext, ext2 i xia tak, by zwiększyć efektywność systemu.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
%{?with_static:%{__make} OPTI="%{rpmcflags}" LDFLAGS="%{rpmldflags}" CC="%{__cc}"}
%{!?with_static:%{__make} OPTI="%{rpmcflags}" LDFLAGS="%{rpmldflags}" CC="%{__cc}" e2defrag defrag e2dump frag}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/sbin,%{_mandir}/man8}

%{__make} %{?with_static:install}%{!?with_static:install_shared} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS ChangeLog NEWS README
%attr(750,root,root) /sbin/e2defrag*
%attr(750,root,root) /sbin/defrag
%attr(750,root,root) /sbin/e2dump
%attr(750,root,root) /sbin/frag
%{_mandir}/man8/*
