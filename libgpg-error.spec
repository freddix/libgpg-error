Summary:	Library libgpg-error
Name:		libgpg-error
Version:	1.16
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	ftp://ftp.gnupg.org/gcrypt/libgpg-error/%{name}-%{version}.tar.bz2
# Source0-md5:	ec7f82d92329a535a89b06142e625f8c
URL:		http://www.gnupg.org/related_software/libgpg-error/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgpg-error is a library that defines common error values for all
GnuPG components. Among these are GPG, GPGSM, GPGME, GPG-Agent,
libgcrypt, pinentry, SmartCard Daemon and possibly more in the future.

%package devel
Summary:	Header files for libgpg-error
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files needed to develop programs that
use these libgpg-error.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%check
%{__make} -j1 check

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog NEWS AUTHORS
%attr(755,root,root) %{_bindir}/gpg-error
%attr(755,root,root) %ghost %{_libdir}/libgpg-error.so.0
%attr(755,root,root) %{_libdir}/libgpg-error.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gpg-error-config
%attr(755,root,root) %{_libdir}/libgpg-error.so
%{_libdir}/libgpg-error.la
%{_includedir}/*.h
%{_aclocaldir}/*.m4

