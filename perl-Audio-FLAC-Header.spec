#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Audio
%define	pnam	FLAC-Header
Summary:	Audio::FLAC::Header - interface to FLAC header metadata
Summary(pl.UTF-8):	Audio::FLAC::HEADER - interfejs do metadanych nagłówków FLAC
Name:		perl-Audio-FLAC-Header
Version:	2.4
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Audio/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	743292694c050be1b10fb4a307f81e87
URL:		http://search.cpan.org/dist/Audio-FLAC-Header/
BuildRequires:	flac-devel
BuildRequires:	perl-Test-Pod-Coverage
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module returns a hash containing basic information about a FLAC
file, a representation of the embedded cue sheet if one exists, as
well as tag information contained in the FLAC file's Vorbis tags.

%description -l pl.UTF-8
Ten moduł zwraca hasza zawierającego podstawowe informacje o pliku
FLAC reprezentujące osadzone wskazówki, a także informacje ze
znaczników Vorbis zawartych w pliku FLAC.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%dir %{perl_vendorarch}/Audio/FLAC
%{perl_vendorarch}/Audio/FLAC/Header.pm
%dir %{perl_vendorarch}/auto/Audio/FLAC
%dir %{perl_vendorarch}/auto/Audio/FLAC/Header
%{perl_vendorarch}/auto/Audio/FLAC/Header/Header.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Audio/FLAC/Header/Header.so
%{_mandir}/man3/*
