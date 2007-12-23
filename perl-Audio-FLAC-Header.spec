#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Audio
%define	pnam	FLAC-Header
Summary:	Audio::FLAC::Header - interface to FLAC header metadata.
#Summary(pl.UTF-8):	
Name:		perl-Audio-FLAC-Header
Version:	1.9
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Audio/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	010bfe368d08ef9c8ef974b43895e9c6
# generic URL, check or change before uncommenting
URL:		http://search.cpan.org/dist/Audio-FLAC-Header/
BuildRequires:	flac-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module returns a hash containing basic information about a FLAC file,
a representation of the embedded cue sheet if one exists,  as well as tag 
information contained in the FLAC file's Vorbis tags.
There is no complete list of tag keys for Vorbis tags, as they can be
defined by the user; the basic set of tags used for FLAC files include:

	ALBUM
	ARTIST
	TITLE
	DATE
	GENRE
	TRACKNUMBER
	COMMENT

The information returned by Audio::FLAC::info is keyed by:

	MINIMUMBLOCKSIZE
	MAXIMUMBLOCKSIZE
	MINIMUMFRAMESIZE
	MAXIMUMFRAMESIZE
	TOTALSAMPLES
	SAMPLERATE
	NUMCHANNELS
	BITSPERSAMPLE
	MD5CHECKSUM

Information stored in the main hash that relates to the file itself or is
calculated from some of the information fields is keyed by:



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
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
