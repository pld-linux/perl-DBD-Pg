%include	/usr/lib/rpm/macros.perl
Summary:	DBD-Pg perl module
Summary(pl):	Modu³ perla DBD-Pg
Name:		perl-DBD-Pg
Version:	0.96
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBD/DBD-Pg-%{version}.tar.gz
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
%setup -q -n DBD-Pg-%{version}

%build
POSTGRES_LIB="/usr/lib"; export POSTGRES_LIB
POSTGRES_INCLUDE="/usr/include/pgsql"; export POSTGRES_INCLUDE
perl Makefile.PL
%{__make} OPTIMIZE="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O0 -g}"

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
