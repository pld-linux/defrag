Summary:	Linux filesystem defragmenter
Name:		defrag
Version:	0.73
Release:	1
Copyright:	GPL
Group:		Utilities/System
Source:		ftp://sunsite.unc.edu/pub/Linux/system/filesystems/%{name}-%{version}.tar.gz
Patch0:		defrag-0.73-glibc.patch
Patch1:		defrag-makefile.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Linux filesystem defragmenters.
The programs in this package will reorganise data on minix, ext, ext2
and xia file system partitions in order to improve the file system's
performance.

%description -l pl
Programy do defragmentacji systemu plików Linuksa.
Zawarte w tym pakiecie programy maj± za zadanie reorganizacjê danych na
partycjach minix, ext, ext2 i xia tak, by zwiêkszyæ efektywno¶æ systemu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
make OPTI="$RPM_OPT_FLAGS" LDFLAGS=-s

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/sbin,%{_mandir}/man8}
make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/* \
	BUGS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (644,root,root,755)
%doc {BUGS,ChangeLog,NEWS,README}.gz
%attr(750,root,root) /sbin/e2defrag
%attr(750,root,root) /sbin/e2defrag.static
%attr(750,root,root) /sbin/defrag
%attr(750,root,root) /sbin/e2dump
%attr(750,root,root) /sbin/frag
%{_mandir}/man8/*.gz
