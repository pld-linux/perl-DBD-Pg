%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	Pg
%define		_noautoreq "perl(POSIX(qw(isprint)))"
Summary:	DBD-Pg perl module
Summary(pl):	Modu³ perla DBD-Pg
Name:		perl-DBD-Pg
Version:	1.01
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-DBI
BuildRequires:	postgresql-libs
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

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/DBD/*.pm
%{perl_sitearch}/auto/DBD/Pg/Pg.bs
%attr(755,root,root) %{perl_sitearch}/auto/DBD/Pg/Pg.so
%{_mandir}/man[13]/*
