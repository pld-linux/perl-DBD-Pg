%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	Pg
%define		_noautoreq "perl(POSIX(qw(isprint)))"
Summary:	DBD::Pg perl module
Summary(pl):	Modu³ perla DBD::Pg
Name:		perl-DBD-Pg
Version:	1.13
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-DBI
BuildRequires:	postgresql-libs
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::Pg - PostgreSQL database driver for the DBI module.

%description -l pl
DBD::Pg - Sterownik bazy danych PostgreSQL dla modu³u DBI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
POSTGRES_LIB="%{_libdir}"; export POSTGRES_LIB
POSTGRES_INCLUDE="%{_includedir}/postgresql"; export POSTGRES_INCLUDE
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitearch}/DBD/*
%dir %{perl_sitearch}/auto/DBD/Pg
%{perl_sitearch}/auto/DBD/Pg/Pg.bs
%attr(755,root,root) %{perl_sitearch}/auto/DBD/Pg/Pg.so
%{_mandir}/man[13]/*
