Summary:	FFmpeg version of headers required to interface with Nvidia codec APIs (NVENC)
Name:     ffnvcodec-headers
Version:	9.0.18.1
Release:	1
License:	MIT
Group:		Development/C
Url:		https://git.videolan.org/?p=ffmpeg/nv-codec-headers.git
Source0:	https://github.com/FFmpeg/nv-codec-headers/releases/download/n%{version}/nv-codec-headers-%{version}.tar.gz
BuildArch:	noarch

%description
FFmpeg version of headers required to interface with Nvidia codec APIs (NVENC)

%files
%doc README
#{_datadir}/pkgconfig/ffnvcodec.pc
#{_includedir}/ffnvcodec/*.h

#----------------------------------------------------------------------------

%prep
%setup -qn nv-codec-headers-n%{version}

%build
make PREFIX=%{_prefix}

%install
%make_install
	LIBDIR=/share \
	PREFIX=%{_prefix}
