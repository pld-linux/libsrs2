Summary:	Next generation SRS library
Summary(pl.UTF-8):	Biblioteka SRS nowej generacji
Name:		libsrs2
Version:	1.0.17
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://www.libsrs2.org/srs/%{name}-%{version}.tar.gz
# Source0-md5:	6c2384e1ef1448777d7e72f98e449423
URL:		http://srs.mirtol.com/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libsrs2 is the next generation SRS library from the original designer
of SRS. It implements the Sender Rewriting Scheme, a part of the
SPF/SRS protocol pair. Libsrs2 has been written from an entirely clean
codebase with compliance, speed and versatility in mind. It is
platform independent and has no external dependencies. It is
thread-safe and heap-safe, and is suitable for large scale
applications and embedded systems and can operate without many
standard system facilities.

%description -l pl.UTF-8
Libsrs2 jest biblioteką SRS nowej generacji. Implementuje Sender
Rewriting Scheme, część pary protokołów SPF/SRS. Libsrs2 została
napisana od zera z myślą o zgodności, szybkości i uniwersalności. Jest
niezależna od platformy i nie ma zewnętrznych zależności. Nadaje się
do użytku w programach wielowątkowych, jest bezpieczna dla stosu, jest
odpowiednia tak dla systemów dużych jak i wbudowanych.

%package devel
Summary:	Header files for libsrs2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libsrs2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libsrs2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libsrs2.

%package static
Summary:	Static libsrs2 library
Summary(pl.UTF-8):	Statyczna biblioteka libsrs2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libsrs2 library.

%description static -l pl.UTF-8
Statyczna biblioteka libsrs2.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
