Summary:	FFmpeg version of headers required to interface with Nvidia codec APIs (NVENC)
Name:     ffnvcodec-headers
Version:	9.1.23.1
Release:	2
License:	MIT
Group:		Development/C
Url:		https://git.videolan.org/?p=ffmpeg/nv-codec-headers.git
Source0:	https://github.com/FFmpeg/nv-codec-headers/releases/download/n%{version}/nv-codec-headers-%{version}.tar.gz
# Can't be noarch because of %{_libdir} location. If a 32-bit built
# version of the package is installed on a 64-bit platform, the pkgconfig
# file won't be found.
#BuildArch:	noarch

%description
FFmpeg version of headers required to interface with Nvidia codec APIs (NVENC)

%files
%doc README
%{_includedir}/ffnvcodec*
%{_libdir}/pkgconfig/ffnvcodec.pc

#----------------------------------------------------------------------------

%prep
%setup -qn nv-codec-headers-%{version}

%build
make PREFIX=%{_prefix}

%install
make PREFIX=%{_prefix} LIBDIR=%{_lib} DESTDIR=%{buildroot} install
