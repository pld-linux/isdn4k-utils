Summary:	Utilities for the kernel ISDN-subsystem
Summary(pl):	U¿ytki dla podsystemu ISDN j±dra
Summary(pt_BR):	Utilitários para configuração do subsistema ISDN
Name:		isdn4k-utils
Version:	0208190200
Release:	2
License:	GPL v2
Group:		Applications/Communications
Source0:	ftp://ftp.suse.com/pub/isdn4linux/v2.1/isdn4k-utils/%{name}-%{version}.tar.gz
Source1:        %{name}.config
Patch0:		%{name}-make.patch
Patch1:		%{name}-ppc.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	ncurses-devel
URL:		http://www.isdn4linux.de/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Utilities for the kernel ISDN-subsystem and some contributions.

%description -l pl
Narzêdzia dla podsystemu ISDN j±dra.

%description -l pt_BR
Utilitários para configuração do subsistema ISDN.

%package x11
Summary:        Utilities for the kernel ISDN-subsystem - frontend for X11
Summary(pl):    U¿ytki dla podsystemu ISDN j±dra - nakladki dla X11.
Group:          Applications/Communications
Requires:       %{name} = %{version}

%description x11
Utilities for the kernel ISDN-subsystem and some contributions (X11).

%description -l pl x11
Narzêdzia dla podsystemu ISDN j±dra, nak³adki graficzne (X11).

%package devel
Summary:	Developement files for isdn4k-tools
Summary(pl):	Rzeczy potrzebne do tworzenia z u¿yciem isdn4k-tools
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Developement files for isdn4k-tools.

%description -l pl devel
Rzeczy potrzebne do tworzenia z u¿yciem isdn4k-tools.

%package static
Summary:	Static libraries for isdn4k-tools
Summary(pl):	Statyczne biblioteki dla isdn4k-tools
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description static
Static libraries for isdn4k-tools.

%description -l pl static
Statyczne biblioteki dla isdn4k-tools.

%prep
%setup -q -n %{name}
%patch0 -p1
%ifarch ppc
%patch1 -p1
%endif

%build
for i in capi20 capifax capiinfo capiinit rcapid; do
	cd $i
	rm -f missing
	%{__libtoolize}
	aclocal
	%{__autoconf}
	%{__automake}
	cd ..
done
cp %{SOURCE1} .config
%{__make} OPTIM="%{rpmcflags}" subconfig
%{__make} CFLAGS="%{rpmcflags} -I/usr/include/ncurses/"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/var/lock/isdn,%{_datadir}/doc/%{name}-%{version}/faq,%{_prefix}/X11R6/bin}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

mv $RPM_BUILD_ROOT%{_datadir}/doc/isdn4linux/faq/*.txt \
	$RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}/faq
mv $RPM_BUILD_ROOT%{_datadir}/doc/isdn4linux/faq/*.html \
	$RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}/faq
mv $RPM_BUILD_ROOT%{_datadir}/doc/vbox/*.txt \
	$RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}
mv $RPM_BUILD_ROOT%{_bindir}/{xisdnload,xmonisdn} \
	$RPM_BUILD_ROOT%{_prefix}/X11R6/bin


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README FAQ NEWS LEGAL.ipppcomp ipppcomp/README.LZS Mini-FAQ/*.txt
%doc isdnlog/{tools/dest/README*,isdnrep/CHANGES*}
%doc FAQ/{_howto,_example}
%config %{_sysconfdir}/isdn/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%{_libdir}/isdn/*
%dir /var/lock/isdn
%dir %{_sysconfdir}/isdn
%dir %{_libdir}/isdn
%{_mandir}/man[14578]/*


%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/X11R6/bin/*
/usr/X11R6/lib/X11/app-defaults/XISDNLoad
/usr/X11R6/man/man1/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.la
%{_includedir}/*.h
/usr/X11R6/include/X11/bitmaps/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
