Summary:	Linux filesystem defragmenter
Summary(pl):	Narzêdzia do defragmentacji linuksowych systemów plików
Name:		defrag
Version:	0.73
Release:	2
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/filesystems/%{name}-%{version}.tar.gz
Patch0:		%{name}-0.73-glibc.patch
Patch1:		%{name}-makefile.patch
Patch2:		%{name}-kernel-2.4.patch
Patch3:		%{name}-shared.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux filesystem defragmenters. The programs in this package will
reorganise data on minix, ext, ext2 and xia file system partitions in
order to improve the file system's performance.

%description -l pl
Programy do defragmentacji systemu plików Linuksa. Zawarte w tym
pakiecie programy maj± za zadanie reorganizacjê danych na partycjach
minix, ext, ext2 i xia tak, by zwiêkszyæ efektywno¶æ systemu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{?!bcond_off_static:%{__make} OPTI="%{rpmcflags}" LDFLAGS="%{rpmldflags}}
%{?bcond_off_static:%{__make} OPTI="%{rpmcflags}" LDFLAGS="%{rpmldflags} e2defrag defrag e2dump frag}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/sbin,%{_mandir}/man8}

%{__make} %{?!bcond_off_static:install}%{?bcond_off_static:install_shared} \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf BUGS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,ChangeLog,NEWS,README}.gz
%attr(750,root,root) /sbin/e2defrag*
%attr(750,root,root) /sbin/defrag
%attr(750,root,root) /sbin/e2dump
%attr(750,root,root) /sbin/frag
%{_mandir}/man8/*
