#
# spec file for package ffmpeg-7
#
# Copyright (c) 2026 SUSE LLC and contributors
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define flavor %nil
#
# preamble is present twice, watch out
#
%if "%flavor" != "ffmpeg-7-mini"

# Create proper conflicts to make sure we require all from one version
# p:   Conflict string, eg if you need them all for requires instead
#      Default value Conflicts:
# c:   copmare string ie "<" or ">=", must be defined
# v:   version string ie. "< 42.3.4" or ">= 15.0.2.1", must be defined
%define devel_conflicts(p:c:v:) \
%define preamble_string %{-p:%{-p*}}%{!-p:Conflicts:} \
%define comparator %{-c:%{-c*}}%{!-c:%{error:Comparator not defined}} \
%define conflicts_version %{-v:%{-v*}}%{!-v:%{error:Version not defined}} \
\
%preamble_string libavcodec-devel %comparator %conflicts_version \
%preamble_string libavdevice-devel %comparator %conflicts_version \
%preamble_string libavfilter-devel %comparator %conflicts_version \
%preamble_string libavformat-devel %comparator %conflicts_version \
%preamble_string libavutil-devel %comparator %conflicts_version \
%preamble_string libpostproc-devel %comparator %conflicts_version \
%preamble_string libswresample-devel %comparator %conflicts_version \
%preamble_string libswscale-devel %comparator %conflicts_version \
%nil

%if 0%{?BUILD_ORIG}
%bcond_without amf_sdk
%bcond_without cuda_sdk
%else
# If software H264 is disabled, the hw driver must be as well:
# HW drivers can fail to initialize, namely when the hardware is absent.
# Browsers choose video formats on sites like youtube based on `ffmpeg
# -codecs` rather than the success/failure status of libav* initialization.
# This becomes a problem when a format only has a HW driver;
# the browser thinks it can do H264 but never succeeds.
%bcond_with    amf_sdk
%bcond_with    cuda_sdk
%endif

%bcond_with    amrwb
%bcond_with    fdk_aac_dlopen
%bcond_with    opencore
%bcond_with    smbclient
%bcond_with    vvenc
%bcond_with    x264
%bcond_with    x265
%bcond_with    xvid

%if 0%{?suse_version} >= 1699
%bcond_without mysofa
%bcond_without vidstab
%bcond_without codec2
%bcond_without rubberband
%bcond_without vulkan
%bcond_without amrwb
%bcond_without opencore
%bcond_without xvid
%else
%if 0%{?suse_version} > 1500
%bcond_without mysofa
%bcond_without vidstab
%bcond_without codec2
%bcond_without rubberband
%bcond_without vulkan
%bcond_without amrwb
%bcond_without opencore
%else
%bcond_with mysofa
%bcond_with vidstab
%bcond_with codec2
%bcond_with rubberband
%bcond_with vulkan
%endif
%endif

%define _name ffmpeg
%define _major_version 7
%define _major_expected 8

Name:           ffmpeg-7
Version:        7.1.5
Release:        0
Summary:        Set of libraries for working with various multimedia formats
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
#Git-Clone:     git://source.ffmpeg.org/ffmpeg
URL:            https://ffmpeg.org/
Source:         https://www.ffmpeg.org/releases/%_name-%version.tar.xz
Source2:        https://www.ffmpeg.org/releases/%_name-%version.tar.xz.asc
Source3:        ffmpeg-7-rpmlintrc
Source4:        enable_decoders
Source5:        enable_encoders
Source6:        ffmpeg-dlopen-headers.tar.xz
Source92:       ffmpeg_get_dlopen_headers.sh
Source98:       http://ffmpeg.org/ffmpeg-devel.asc#/ffmpeg-7.keyring
Source99:       baselibs.conf
Patch1:         ffmpeg-arm6l.diff
Patch2:         ffmpeg-new-coder-errors.diff
Patch3:         ffmpeg-codec-choice.diff
Patch4:         ffmpeg-4.2-dlopen-fdk_aac.patch
Patch5:         work-around-abi-break.patch
Patch6:         ffmpeg-chromium.patch
Patch7:         11013-avcodec-decode-clean-up-if-get_hw_frames_parameters-.patch
Patch8:         ffmpeg-7-CVE-2026-64835.patch
Patch9:         ffmpeg-7-CVE-2026-64832.patch
Patch10:        ffmpeg-7-CVE-2026-64830.patch
Patch11:        ffmpeg-7-CVE-2026-66038.patch
Patch12:        ffmpeg-7-CVE-2026-66039.patch
Patch13:        ffmpeg-7-CVE-2026-66041.patch
Patch14:        ffmpeg-7-CVE-2026-58049.patch
Patch15:        ffmpeg-7-CVE-2026-64833.patch
Patch16:        ffmpeg-7-CVE-2026-64834.patch
Patch17:        ffmpeg-7-CVE-2026-65703.patch
Patch18:        ffmpeg-7-CVE-2026-65704.patch
Patch19:        ffmpeg-7-CVE-2026-65705.patch
Patch20:        ffmpeg-7-CVE-2026-65706.patch
Patch21:        ffmpeg-7-CVE-2026-66036-shim01.patch
Patch22:        ffmpeg-7-CVE-2026-66036-shim02.patch
Patch23:        ffmpeg-7-CVE-2026-66036.patch
Patch24:        ffmpeg-7-CVE-2026-66037.patch
Patch25:        ffmpeg-7-CVE-2026-70628.patch
Patch26:        ffmpeg-7-CVE-2026-70629.patch
Patch27:        ffmpeg-7-CVE-2026-70630.patch
Patch28:        ffmpeg-7-CVE-2026-70631.patch
Patch29:        ffmpeg-7-CVE-2026-70632.patch
Patch30:        ffmpeg-7-CVE-2026-75141.patch
Patch31:        ffmpeg-7-CVE-2026-75142.patch
Patch32:        ffmpeg-7-CVE-2026-75143.patch
Patch33:        ffmpeg-7-CVE-2026-75144.patch
Patch34:        ffmpeg-7-CVE-2026-75146.patch
Patch35:        ffmpeg-7-CVE-2026-38345.patch
Patch36:        ffmpeg-7-CVE-2026-38350_part01_aca41d3.patch
Patch37:        ffmpeg-7-CVE-2026-38350_part02_c44d237.patch
# There is another Patch section further below!
BuildRequires:  ladspa-devel
BuildRequires:  libgsm-devel
BuildRequires:  nasm
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(aom) >= 1.0.0
BuildRequires:  pkgconfig(dav1d) >= 0.5.0
BuildRequires:  pkgconfig(ffnvcodec) >= 8.1.24.15
BuildRequires:  pkgconfig(fontconfig) >= 2.4.2
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi) >= 0.19.0
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libass) >= 0.11.0
BuildRequires:  pkgconfig(libavc1394)
BuildRequires:  pkgconfig(libbluray)
BuildRequires:  pkgconfig(libbs2b)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libcdio_paranoia)
BuildRequires:  pkgconfig(libdc1394-2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libgme)
BuildRequires:  pkgconfig(libiec61883)
BuildRequires:  pkgconfig(libmp3lame) >= 3.98.3
BuildRequires:  pkgconfig(libopenjp2) >= 2.1.0
BuildRequires:  pkgconfig(libopenmpt) >= 0.2.6557
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libraw1394)
BuildRequires:  pkgconfig(libssh) >= 0.6.0
BuildRequires:  pkgconfig(libva) >= 0.35.0
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(libvmaf) >= 2.0.0
BuildRequires:  pkgconfig(libwebp) >= 0.4
BuildRequires:  pkgconfig(libwebpmux) >= 0.4.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzmq) >= 4.2.1
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openh264)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(sdl2) >= 2.0.1
BuildRequires:  pkgconfig(soxr)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(srt) >= 1.3.0
BuildRequires:  pkgconfig(theora) >= 1.1
BuildRequires:  pkgconfig(twolame) >= 0.3.10
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vpx) >= 1.4.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(zimg) >= 2.7.0
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(zvbi-0.2) >= 0.2.28

%if %{with amf_sdk}
BuildRequires:  AMF-devel
%endif
%if %{with mysofa}
BuildRequires:  pkgconfig(libmysofa)
%endif
%if %{with codec2}
BuildRequires:  pkgconfig(codec2)
%endif
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150700
BuildRequires:  pkgconfig(libjxl) >= 0.7.0
BuildRequires:  pkgconfig(libjxl_threads) >= 0.7.0
BuildRequires:  pkgconfig(librist) >= 0.2.7
%endif
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
BuildRequires:  pkgconfig(rav1e) >= 0.5.0
%endif
%if %{with rubberband}
BuildRequires:  pkgconfig(rubberband) >= 1.8.1
%endif
%if %{with smbclient}
BuildRequires:  pkgconfig(smbclient)
%endif
%if %{with vidstab}
BuildRequires:  pkgconfig(vidstab) >= 0.98
%endif
%if %{with fdk_aac_dlopen}
BuildRequires:  pkgconfig(fdk-aac)
%endif
%if %{with xvid}
BuildRequires:  libxvidcore-devel
%endif
%if %{with opencore}
BuildRequires:  pkgconfig(opencore-amrnb)
%endif
%if %{with amrwb}
BuildRequires:  pkgconfig(vo-amrwbenc)
%endif
%if %{with vvenc}
BuildRequires:  vvenc-devel
%endif
%if %{with x264}
BuildRequires:  pkgconfig(x264)
%endif
%if %{with x265}
BuildRequires:  pkgconfig(x265)
%endif

%ifarch x86_64 %x86_64 aarch64
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150500
BuildRequires:  pkgconfig(SvtAv1Enc) >= 0.9.0
%endif
%endif

%if %{with vulkan}
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150600
BuildRequires:  pkgconfig(libplacebo) >= 6.292.0
%else
BuildRequires:  (pkgconfig(libplacebo) >= 4.192.0 with pkgconfig(libplacebo) < 6.292.0)
%endif
BuildRequires:  pkgconfig(shaderc) >= 2019.1
BuildRequires:  pkgconfig(vulkan) >= 1.3.255
%endif

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150500
%ifarch x86_64 %x86_64
BuildRequires:  pkgconfig(vpl) >= 2.6
%endif
%endif

Provides:       ffmpeg-tools = %version
Conflicts:      ffmpeg-tools
Provides:       ffmpeg = %version
Obsoletes:      ffmpeg < %version
Requires:       (libavcodec61 = %version-%release or ffmpeg-7-mini-libs = %version-%release)
Requires:       (libavdevice61 = %version-%release or ffmpeg-7-mini-libs = %version-%release)
Requires:       (libavfilter10 = %version-%release or ffmpeg-7-mini-libs = %version-%release)
Requires:       (libavformat61 = %version-%release or ffmpeg-7-mini-libs = %version-%release)
Requires:       (libavutil59 = %version-%release or ffmpeg-7-mini-libs = %version-%release)
Requires:       (libpostproc58 = %version-%release or ffmpeg-7-mini-libs = %version-%release)
Requires:       (libswresample5 = %version-%release or ffmpeg-7-mini-libs = %version-%release)
Requires:       (libswscale8 = %version-%release or ffmpeg-7-mini-libs = %version-%release)

%description
FFmpeg is a multimedia framework, able to decode, encode,
transcode, mux, demux, stream, filter and play several formats
that humans and machines have created.
%if !0%{?BUILD_ORIG}

This build of ffmpeg is limited in the number of codecs supported.
%endif

%package -n libavcodec61
Summary:        FFmpeg codec library
Group:          System/Libraries
Requires:       libavutil59 = %version-%release
Requires:       libswresample5 = %version-%release
%if 0%{?BUILD_ORIG}
Provides:       libavcodec-full = %version-%release
# This can be (and is) required by packages like vlc-codecs -
# do follow the shlib name to not get random lib providers
Provides:       libavcodec61(unrestricted)
%endif
# For mozillas
Provides:       libavcodec = %version-%release

%description -n libavcodec61
The libavcodec library provides a generic encoding/decoding framework
and contains multiple decoders and encoders for audio, video and
subtitle streams, and several bitstream filters.
%if !0%{?BUILD_ORIG}

This build of ffmpeg is limited in the number of codecs supported.
%endif

%package libavcodec-devel
Summary:        Development files for FFmpeg's codec library
Group:          Development/Libraries/C and C++
Provides:       libavcodec-devel = %version-%release
Obsoletes:      libavcodec-devel < %version-%release
Requires:       %name-libavutil-devel = %version-%release
Requires:       libavcodec61 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libavcodec-devel
The libavcodec library provides a generic encoding/decoding framework
and contains multiple decoders and encoders for audio, video and
subtitle streams, and several bitstream filters.

This subpackage contains the headers for FFmpeg libavcodec.

%package -n libavdevice61
Summary:        FFmpeg device library
Group:          System/Libraries
Requires:       libavcodec61 = %version-%release
Requires:       libavfilter10 = %version-%release
Requires:       libavformat61 = %version-%release
Requires:       libavutil59 = %version-%release

%description -n libavdevice61
The libavdevice library provides a generic framework for grabbing from
and rendering to many common multimedia input/output devices, and
supports several input and output devices, including Video4Linux2, VfW,
DShow, and ALSA.

%package libavdevice-devel
Summary:        Development files for FFmpeg's device library
Group:          Development/Libraries/C and C++
Provides:       ffmpeg-devel = %version-%release
Conflicts:      ffmpeg-devel
Provides:       libavdevice-devel = %version-%release
Obsoletes:      libavdevice-devel < %version-%release
Requires:       %name-libavcodec-devel = %version-%release
Requires:       %name-libavfilter-devel = %version-%release
Requires:       %name-libavformat-devel = %version-%release
Requires:       %name-libavutil-devel = %version-%release
Requires:       %name-libpostproc-devel = %version-%release
Requires:       %name-libswresample-devel = %version-%release
Requires:       %name-libswscale-devel = %version-%release
Requires:       libavdevice61 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libavdevice-devel
The libavdevice library provides a generic framework for grabbing from
and rendering to many common multimedia input/output devices, and
supports several input and output devices, including Video4Linux2, VfW,
DShow, and ALSA.

This subpackage contains the headers for FFmpeg libavcodec.

%package -n libavfilter10
Summary:        FFmpeg audio and video filtering library
Group:          System/Libraries
Requires:       libavcodec61 = %version-%release
Requires:       libavformat61 = %version-%release
Requires:       libavutil59 = %version-%release
Requires:       libpostproc58 = %version-%release
Requires:       libswresample5 = %version-%release
Requires:       libswscale8 = %version-%release

%description -n libavfilter10
The libavfilter library provides a generic audio/video filtering
framework containing several filters, sources and sinks.

%package libavfilter-devel
Summary:        Development files for FFmpeg's audio/video filter library
Group:          Development/Libraries/C and C++
Provides:       libavfilter-devel = %version-%release
Obsoletes:      libavfilter-devel < %version-%release
Requires:       %name-libavcodec-devel = %version-%release
Requires:       %name-libavformat-devel = %version-%release
Requires:       %name-libavutil-devel = %version-%release
Requires:       %name-libpostproc-devel = %version-%release
Requires:       %name-libswresample-devel = %version-%release
Requires:       %name-libswscale-devel = %version-%release
Requires:       libavfilter10 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libavfilter-devel
The libavfilter library provides a generic audio/video filtering
framework containing several filters, sources and sinks.

This subpackage contains the headers for FFmpeg libavfilter.

%package -n libavformat61
Summary:        FFmpeg's stream format library
Group:          System/Libraries
Requires:       libavcodec61 = %version-%release
Requires:       libavutil59 = %version-%release

%description -n libavformat61
The libavformat library provides a generic framework for multiplexing
and demultiplexing (muxing and demuxing) audio, video and subtitle
streams. It encompasses multiple muxers and demuxers for multimedia
container formats.
%if !0%{?BUILD_ORIG}

This build of ffmpeg is limited in the number of codecs supported.
%endif

%package libavformat-devel
Summary:        Development files for FFmpeg's stream format library
Group:          Development/Libraries/C and C++
Provides:       libavformat-devel = %version-%release
Obsoletes:      libavformat-devel < %version-%release
Requires:       %name-libavcodec-devel = %version-%release
Requires:       %name-libavutil-devel = %version-%release
Requires:       %name-libswresample-devel = %version-%release
Requires:       libavformat61 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libavformat-devel
The libavformat library provides a generic framework for multiplexing
and demultiplexing (muxing and demuxing) audio, video and subtitle
streams. It encompasses multiple muxers and demuxers for multimedia
container formats.

This subpackage contains the headers for FFmpeg libavformat.

%package -n libavutil59
Summary:        FFmpeg's utility library
Group:          System/Libraries

%description -n libavutil59
The libavutil library is a utility library to aid portable multimedia
programming. It contains safe portable string functions, random
number generators, data structures, additional mathematics functions,
cryptography and multimedia related functionality (like enumerations
for pixel and sample formats).

%package libavutil-devel
Summary:        Development files for FFmpeg's utility library
Group:          Development/Libraries/C and C++
Provides:       libavutil-devel = %version-%release
Obsoletes:      libavutil-devel < %version-%release
Requires:       libavutil59 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libavutil-devel
The libavutil library is a utility library to aid portable multimedia
programming. It contains safe portable string functions, random
number generators, data structures, additional mathematics functions,
cryptography and multimedia related functionality (like enumerations
for pixel and sample formats).

This subpackage contains the headers for FFmpeg libavutil.

%package -n libpostproc58
Summary:        FFmpeg post-processing library
Group:          System/Libraries
Requires:       libavutil59 = %version-%release

%description -n libpostproc58
A library with video postprocessing filters, such as deblocking and
deringing filters, noise reduction, automatic contrast and brightness
correction, linear/cubic interpolating deinterlacing.

%package libpostproc-devel
Summary:        Development files for the FFmpeg post-processing library
Group:          Development/Libraries/C and C++
Provides:       libpostproc-devel = %version-%release
Obsoletes:      libpostproc-devel < %version-%release
Requires:       %name-libavutil-devel = %version-%release
Requires:       libpostproc58 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libpostproc-devel
A library with video postprocessing filters, such as deblocking and
deringing filters, noise reduction, automatic contrast and brightness
correction, linear/cubic interpolating deinterlacing.

This subpackage contains the headers for FFmpeg libpostproc.

%package -n libswresample5
Summary:        FFmpeg software resampling library
Group:          System/Libraries
Requires:       libavutil59 = %version-%release

%description -n libswresample5
The libswresample library performs audio conversion between different
sample rates, channel layout and channel formats.

%package libswresample-devel
Summary:        Development files for the FFmpeg software resampling library
Group:          Development/Libraries/C and C++
Provides:       libswresample-devel = %version-%release
Obsoletes:      libswresample-devel < %version-%release
Requires:       %name-libavutil-devel = %version-%release
Requires:       libswresample5 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libswresample-devel
The libswresample library performs audio conversion between different
sample rates, channel layout and channel formats.

This subpackage contains the headers for FFmpeg libswresample.

%package -n libswscale8
Summary:        FFmpeg image scaling and colorspace/pixel conversion library
Group:          System/Libraries
Requires:       libavutil59 = %version-%release

%description -n libswscale8
The libswscale library performs image scaling and colorspace and
pixel format conversion operations.

%package libswscale-devel
Summary:        Development files for FFmpeg's image scaling and colorspace library
Group:          Development/Libraries/C and C++
Conflicts:      libswscale-devel
Provides:       libswscale-devel = %version-%release
Requires:       %name-libavutil-devel = %version-%release
Requires:       libswscale8 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libswscale-devel
The libswscale library performs image scaling and colorspace and
pixel format conversion operations.

This subpackage contains the headers for FFmpeg libswscale.

%prep
%autosetup -p1 -a6 -n %_name-%version

%build
%ifarch %ix86 %arm
%define _lto_cflags %nil
%endif
%if "%_lto_cflags" != ""
%global _lto_cflags %_lto_cflags -ffat-lto-objects
%endif
CFLAGS="%optflags" \
%if 0%{?suse_version} > 1500
%ifarch %ix86
%else
LDFLAGS="%_lto_cflags" \
%endif
%endif
./configure \
	--prefix="%_prefix" \
	--libdir="%_libdir" \
	--shlibdir="%_libdir" \
	--incdir="%_includedir/ffmpeg" \
	--extra-cflags="%optflags" \
	--optflags="%optflags" \
	--disable-htmlpages \
	--enable-pic \
	--disable-stripping \
	--enable-shared \
	--disable-static \
	--enable-gpl \
	--enable-version3 \
%if %{with smbclient}
	--enable-libsmbclient \
%endif
	--disable-openssl \
	--enable-gnutls \
	--enable-ladspa \
%if %{with vulkan}
	--enable-libshaderc \
	--enable-vulkan \
	--enable-libplacebo \
%endif
%if %{with amf}
        --enable-amf \
%endif
%if !%{with cuda_sdk}
	--disable-cuda-sdk \
%endif
	--enable-libaom \
	--enable-libass \
	--enable-libbluray \
	--enable-libbs2b \
	--enable-libcdio \
%if %{with codec2}
	--enable-libcodec2 \
%endif
	--enable-libdav1d \
	--enable-libdc1394 \
	--enable-libdrm \
	--enable-libfontconfig \
	--enable-libfreetype \
	--enable-libfribidi \
	--enable-libgsm \
	--enable-libiec61883 \
	--enable-libjack \
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150700
	--enable-libjxl \
	--enable-librist \
%endif
	--enable-libmp3lame \
%if %{with mysofa}
	--enable-libmysofa \
%endif
	--enable-libopenjpeg \
	--enable-libopenmpt \
	--enable-libopenh264 \
	--enable-libopus \
	--enable-libpulse \
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
	--enable-librav1e \
%endif
%if %{with rubberband}
	--enable-librubberband \
%endif
%ifarch x86_64 %x86_64 aarch64
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150500
	--enable-libsvtav1 \
%endif
%endif
	--enable-libsoxr \
	--enable-libspeex \
	--enable-libssh \
	--enable-libsrt \
	--enable-libtheora \
	--enable-libtwolame \
%if %{with vidstab}
	--enable-libvidstab \
%endif
	--enable-libvmaf \
	--enable-libvorbis \
	--enable-libvpx \
	--enable-libwebp \
	--enable-libxml2 \
	--enable-libzimg \
	--enable-libzmq \
	--enable-libzvbi \
%if 0%{?suse_version} > 1500
%ifarch %ix86
%else
	--enable-lto \
%endif
%endif
	--enable-lv2 \
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150500
%ifarch x86_64 %x86_64
	--enable-libvpl \
%endif
%endif
	--enable-vaapi \
	--enable-vdpau \
	--enable-version3 \
%if %{with fdk_aac_dlopen}
	--enable-libfdk-aac-dlopen \
	--enable-nonfree \
%endif
%if %{with opencore}
	--enable-libopencore-amrnb \
	--enable-libopencore-amrwb \
%endif
%if %{with amrwb}
	--enable-libvo-amrwbenc \
%endif
%if %{with vvenc}
	--enable-libvvenc \
%endif
%if %{with x264}
	--enable-libx264 \
%endif
%if %{with x265}
	--enable-libx265 \
%endif
%if %{with xvid}
	--enable-libxvid \
%endif
%if !0%{?BUILD_ORIG}
	--enable-muxers \
	--enable-demuxers \
	--disable-encoders \
	--disable-decoders \
	--disable-decoder=h264,hevc,vc1,vvc \
	--enable-encoder="$(perl -pe 's{^(\w*).*}{$1,}gs' <%_sourcedir/enable_encoders)" \
	--enable-decoder="$(perl -pe 's{^(\w*).*}{$1,}gs' <%_sourcedir/enable_decoders)" \

for i in H264 HEVC VC1 VVC; do
	grep -q "#define CONFIG_${i}_DECODER 0" config_components.h
done
%endif

cat config.h
%make_build

%global extratools aviocat cws2fws ffescape ffeval ffhash fourcc2pixfmt graph2dot ismindex pktdumper probetest qt-faststart seek_print sidxindex trasher

for i in %extratools; do
	%make_build "tools/$i"
done

%install
b="%buildroot"
%make_install install-man
rm -Rf "$b/%_datadir/ffmpeg/examples"
for i in %extratools; do
	cp -a "tools/$i" "$b/%_bindir/"
done

%ldconfig_scriptlets -n libavcodec61
%ldconfig_scriptlets -n libavdevice61
%ldconfig_scriptlets -n libavfilter10
%ldconfig_scriptlets -n libavformat61
%ldconfig_scriptlets -n libavutil59
%ldconfig_scriptlets -n libpostproc58
%ldconfig_scriptlets -n libswresample5
%ldconfig_scriptlets -n libswscale8

%files
%doc Changelog CREDITS README.md
%_bindir/*
%_mandir/man1/ff*.1*
%_datadir/ffmpeg/

%files -n libavcodec61
%license COPYING.GPLv2 LICENSE.md
%_libdir/libavcodec.so.*

%files -n libavdevice61
%license COPYING.GPLv2 LICENSE.md
%_libdir/libavdevice.so.*

%files -n libavfilter10
%license COPYING.GPLv2 LICENSE.md
%_libdir/libavfilter.so.*

%files -n libavformat61
%license COPYING.GPLv2 LICENSE.md
%_libdir/libavformat.so.*

%files -n libavutil59
%license COPYING.GPLv2 LICENSE.md
%_libdir/libavutil.so.*

%files -n libpostproc58
%license COPYING.GPLv2 LICENSE.md
%_libdir/libpostproc.so.*

%files -n libswresample5
%license COPYING.GPLv2 LICENSE.md
%_libdir/libswresample.so.*

%files -n libswscale8
%license COPYING.GPLv2 LICENSE.md
%_libdir/libswscale.so.*

%files libavcodec-devel
%dir %_includedir/ffmpeg/
%_includedir/ffmpeg/libavcodec/
%_libdir/libavcodec.so
%_libdir/pkgconfig/libavcodec.pc
%_mandir/man3/libavcodec.3*

%files libavdevice-devel
%dir %_includedir/ffmpeg/
%_includedir/ffmpeg/libavdevice/
%_libdir/libavdevice.so
%_libdir/pkgconfig/libavdevice.pc
%_mandir/man3/libavdevice.3*

%files libavfilter-devel
%dir %_includedir/ffmpeg/
%_includedir/ffmpeg/libavfilter/
%_libdir/libavfilter.so
%_libdir/pkgconfig/libavfilter.pc
%_mandir/man3/libavfilter.3*

%files libavformat-devel
%dir %_includedir/ffmpeg/
%_includedir/ffmpeg/libavformat/
%_libdir/libavformat.so
%_libdir/pkgconfig/libavformat.pc
%_mandir/man3/libavformat.3*

%files libavutil-devel
%dir %_includedir/ffmpeg/
%_includedir/ffmpeg/libavutil/
%_libdir/libavutil.so
%_libdir/pkgconfig/libavutil.pc
%_mandir/man3/libavutil.3*

%files libpostproc-devel
%dir %_includedir/ffmpeg/
%_includedir/ffmpeg/libpostproc/
%_libdir/libpostproc.so
%_libdir/pkgconfig/libpostproc.pc

%files libswresample-devel
%dir %_includedir/ffmpeg/
%_includedir/ffmpeg/libswresample/
%_libdir/libswresample.so
%_libdir/pkgconfig/libswresample.pc
%_mandir/man3/libswresample.3*

%files libswscale-devel
%dir %_includedir/ffmpeg/
%_includedir/ffmpeg/libswscale/
%_libdir/libswscale.so
%_libdir/pkgconfig/libswscale.pc
%_mandir/man3/libswscale.3*

%else
%define _name ffmpeg
# Patches may subtly change internal APIs, so we're sticking %%release in
# Requires lines. It also conveniently blocks openSUSE libav* being combined
# with Packman libav*, due to PM's unique %%release numbers.
# This use of %%release with %flavor however requires bcnt synchro:
#
#!BcntSyncTag:  ffmpeg-7
Name:           ffmpeg-7-mini
Version:        7.1.5
Release:        0
Summary:        Set of libraries for working with various multimedia formats
License:        GPL-3.0-or-later
URL:            https://ffmpeg.org/
#Git-Clone:     git://source.ffmpeg.org/ffmpeg
Source:         https://www.ffmpeg.org/releases/%_name-%version.tar.xz
Source2:        https://www.ffmpeg.org/releases/%_name-%version.tar.xz.asc
Source3:        ffmpeg-7-rpmlintrc
Source98:       http://ffmpeg.org/ffmpeg-devel.asc#/ffmpeg-7.keyring
Patch1:         ffmpeg-arm6l.diff
Patch2:         ffmpeg-new-coder-errors.diff
Patch3:         ffmpeg-codec-choice.diff
Patch4:         ffmpeg-4.2-dlopen-fdk_aac.patch
Patch5:         work-around-abi-break.patch
Patch6:         ffmpeg-chromium.patch
Patch7:         11013-avcodec-decode-clean-up-if-get_hw_frames_parameters-.patch
Patch8:         ffmpeg-7-CVE-2026-64835.patch
Patch9:         ffmpeg-7-CVE-2026-64832.patch
Patch10:        ffmpeg-7-CVE-2026-64830.patch
Patch11:        ffmpeg-7-CVE-2026-66038.patch
Patch12:        ffmpeg-7-CVE-2026-66039.patch
Patch13:        ffmpeg-7-CVE-2026-66041.patch
BuildRequires:  c_compiler
BuildRequires:  pkgconfig(openh264)
Requires:       this-is-only-for-build-envs

%description
FFmpeg is a multimedia framework.
This package merely builds the API for the sake of other packages.

%package libs
# Even with mini, we want ff5 libs to be coinstallable to ff4-devel(!),
# hence mini-libs and mini-devel are still separated.
Summary:        Feature-reduced build of FFmpeg, a multimedia framework
Conflicts:      libavcodec61
Conflicts:      libavdevice61
Conflicts:      libavfilter10
Conflicts:      libavformat61
Conflicts:      libavutil59
Conflicts:      libpostproc58
Conflicts:      libswresample5
Conflicts:      libswscale8
Requires:       this-is-only-for-build-envs

%description libs
FFmpeg is a multimedia framework.
This package contains a cut-down version for building other packages.

%package devel
Summary:        Header files for feature-reduced FFmpeg build
Provides:       libavcodec-devel = %version-%release
Conflicts:      libavcodec-devel
Provides:       libavdevice-devel = %version-%release
Conflicts:      libavdevice-devel
Provides:       libavfilter-devel = %version-%release
Conflicts:      libavfilter-devel
Provides:       libavformat-devel = %version-%release
Conflicts:      libavformat-devel
Provides:       libavutil-devel = %version-%release
Conflicts:      libavutil-devel
Provides:       libpostproc-devel = %version-%release
Conflicts:      libpostproc-devel
Provides:       libswresample-devel = %version-%release
Conflicts:      libswresample-devel
Provides:       libswscale-devel = %version-%release
Conflicts:      libswscale-devel
Requires:       %name-libs = %version-%release
Requires:       this-is-only-for-build-envs

%description devel
FFmpeg is a multimedia framework.
This package contains the headers accompanying %name.

%prep
%autosetup -p1 -n %_name-%version

%build
%define _lto_cflags %nil
CFLAGS="%optflags" \
./configure \
	--prefix="%_prefix" \
	--libdir="%_libdir" \
	--shlibdir="%_libdir" \
	--incdir="%_includedir/ffmpeg" \
	--extra-cflags="%optflags" \
	--optflags="%optflags" \
	--disable-htmlpages --disable-stripping --disable-x86asm \
	--disable-static --enable-shared --enable-pic \
	--enable-gpl --enable-version3 \
	--disable-muxers --disable-demuxers \
	--disable-encoders --disable-decoders \
	--disable-programs --disable-doc
for i in H264 HEVC VC1 VVC; do
	grep -q "#define CONFIG_${i}_DECODER 0" config_components.h
done
cat config.h
%make_build

%install
b="%buildroot"
%make_install
rm -Rf "$b/%_datadir/ffmpeg/examples"

%ldconfig_scriptlets libs

%files libs
%_libdir/libavcodec.so.*
%_libdir/libavdevice.so.*
%_libdir/libavfilter.so.*
%_libdir/libavformat.so.*
%_libdir/libavutil.so.*
%_libdir/libpostproc.so.*
%_libdir/libswresample.so.*
%_libdir/libswscale.so.*

%files devel
%license COPYING.GPLv2 LICENSE.md
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_includedir/ffmpeg/

%endif

%changelog
* Mon Oct 12 2026 Jan Engelhardt <jengelh@inai.de>
- Synchronize codec enablement list from ffmpeg-9
* Mon Oct 12 2026 Bjørn Lie <bjorn.lie@gmail.com>
- Enable RealAudio Lossless, RealVideo 3.0 and 4.0 decoders.
* Fri Sep 11 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2026-38350_part02_c44d237.patch:
  Backport c44d237d from upstream, swscale/output: Fix integer
  overflow with lum/chr/alpha filter.
  (CVE-2026-38350, bsc#1277370)
* Fri Sep 11 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2026-38350_part01_aca41d3.patch:
  Backport aca41d3d from upstream, swscale/output: Fix all bilinear
  integer overflows.
  (CVE-2026-38350, bsc#1277370)
* Fri Sep 11 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2026-38345.patch:
  Backport 04fe9848 from upstream, libswscale/utils: prevent division
  by zero for chroma width 8.
  (CVE-2026-38345, bsc#1277376)
* Fri Aug 28 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2026-75146.patch:
  Backport 65b0dab9 from upstream, avformat/dashdec: reject a negative
  fragment index.
  (CVE-2026-75146, bsc#1276412)
* Fri Aug 28 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2026-75144.patch:
  Backport 1c10bcc2 from upstream, avformat/rtpenc_vc2hq: reject data
  units larger than the RTP payload buffer.
  (CVE-2026-75144, bsc#1276410)
* Fri Aug 28 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2026-75143.patch:
  Backport 1c10bcc2 from upstream, avformat/librist: honor the caller
  buffer size in librist_read.
  (CVE-2026-75143, bsc#1276409)
* Fri Aug 28 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2026-75142.patch:
  Backport 9d786e4b from upstream, avformat/mpegenc: reject stream
  counts that overflow the system header.
  (CVE-2026-75142, bsc#1276408)
* Fri Aug 28 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2026-75141.patch:
  Backport acf5d7cd from upstream, avformat/hevc: reject hvcC
  NAL arrays that overflow the 16-bit count.
  (CVE-2026-75141, bsc#1276407)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2026-70632.patch:
  Backport 16b2049d from upstream, avcodec/cfhd: reject transform-2
  output wider than the plane.
  (CVE-2026-70632, bsc#1274289)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2026-70631.patch:
  Backport 3c287af3 from upstream, avcodec/tiff: reject inflate
  output shorter than the strip.
  (CVE-2026-70631, bsc#1274287)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2026-70630.patch:
  Backport c22667d0 from upstream, avcodec/screenpresso: reject
  deflate output shorter than the frame.
  (CVE-2026-70630, bsc#1274282)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2026-70629.patch:
  Backport a5fe21a1 from upstream, avcodec/rscc: do not leave
  uninitilized data when the input is too short.
  (CVE-2026-70629, bsc#1274270)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2026-70628.patch:
  Backport 02fc47e1 from upstream, avcodec/dvbsub_parser: avoid
  signed overflow in the capacity check.
  (CVE-2026-70628, bsc#1274268)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2026-66037.patch:
  Backport f15e730c from upstream, avformat/iamf_parse: check
  count_label against the available bytes.
  (CVE-2026-66037, bsc#1272764)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2026-66036.patch:
  Backport 62294b6a from upstream, avfilter/vf_hqdn3d: support
  dynamic frame sizes.
  (CVE-2026-66036, bsc#1272763)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2026-66036-shim02.patch
  Backport 4f623b4c from upstream, avfilter/vf_libplacebo: implement
  rotation option. This patch is for facilitate ffmpeg-CVE-2026-66036.patch.
  (CVE-2026-66036, bsc#1272763)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2026-66036-shim01.patch
  Backport e3d0c719 from upstream, avfilter/vf_hqdn3d: reject
  unsupported frame parameter changes. This patch is for facilitate
  ffmpeg-CVE-2026-66036.patch.
  (CVE-2026-66036, bsc#1272763)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2026-65706.patch:
  Backport b3c7ebc1 from upstream, avfilter/vf_swaprect: size the
  temp row buffer for the widest plane.
  (CVE-2026-65706, bsc#1272762)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2026-65705.patch:
  Backport 30a52276 from upstream, avfilter/vf_floodfill: remove
  unneeded variables.
  (CVE-2026-65705, bsc#1272761)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2026-65704.patch:
  Backport 52f7983f from upstream, avformat/ty: don't let the Series2
  AC3 trim underflow the packet size.
  (CVE-2026-65704, bsc#1272760)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2026-65703.patch:
  Backport 3b85fbe8 from upstream, avcodec/tdsc: unref the reference
  frame before reallocating on size change.
  (CVE-2026-65703, bsc#1272759)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2026-64834.patch:
  Backport 3c441711 from upstream, avformat/rtpdec_asf: reject ASF
  objects smaller than their header.
  (CVE-2026-64834, bsc#1272757)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2026-64833.patch:
  Backport 385ac2fa from upstream, avformat/spdifenc: bound DTS
  core_size against the packet size in the HD path.
  (CVE-2026-64833, bsc#1272755)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2026-58049.patch:
  Backport f8d7795d from upstream, avcodec/rasc: Check that 32-bit
  DLTA accesses stay within the row.
  (CVE-2026-58049, bsc#1269550)
* Thu Jul 30 2026 Xiaoguang Wang <xiaoguang.wang@suse.com>
- Add CVE patches:
  ffmpeg-7-CVE-2026-64835.patch: (CVE-2026-64835, bsc#1272758)
  ffmpeg-7-CVE-2026-64832.patch: (CVE-2026-64832, bsc#1272754)
  ffmpeg-7-CVE-2026-64830.patch: (CVE-2026-64830, bsc#1272752)
  ffmpeg-7-CVE-2026-66038.patch: (CVE-2026-66038, bsc#1272768)
  ffmpeg-7-CVE-2026-66039.patch: (CVE-2026-66039, bsc#1272765)
  ffmpeg-7-CVE-2026-66041.patch: (CVE-2026-66041, bsc#1272767)
* Fri Jul 24 2026 Cliff Zhao <qzhao@suse.com>
- Update to version 7.1.5:
  * Various crash, out-of-bounds access, add boundary check
    fixes. Affected: .mov parser, DASH parser, Snow encoder,
    Icecast, RTSP decoder, RV10/RV34 RealVideo, Truespeech,
    ADPCM, Matroska decoder
  * avcodec/jpeg2000dec: clear array length when freeing it
    (CVE-2025-22921, bsc#1237382)
  * avcodec/magicyuv: Fix 1 line MEDIAN slices
    (CVE-2026-8461, bsc#1269490)
  * avcodec/magicyuv: reject slice_height misaligned with chroma vshift.
    (CVE-2026-8461, bsc#1269490)
  * avcodec/magicyuv: Expand the s->interlaced slice-height sanity check.
    (CVE-2026-8461, bsc#1269490)
  * swscale/alphablend: don't overread alpha plane on subsampled odd size
    (CVE-2026-38347, bsc#1277373)
- Drop ffmpeg-7-CVE-2025-22921.patch (merged)
* Fri May 22 2026 Bjørn Lie <bjorn.lie@gmail.com>
- Update to version 7.1.4:
  * Codec, format, filter and various other bugfixes.
  * avcodec/av1dec: check that primary_ref_frame is within range.
    (CVE-2026-30997, bsc#1262047)
  * avcodec/rasc: fix heap use-after-free in decode_move().
    (CVE-2026-12706, bsc#1268595)
  * avcodec/tdsc: remove double stride adjustment
    (CVE-2026-18393, bsc#1277377)
  * swscale/output: Fixes integer overflow in yuv2planeX_8_c.
    (CVE-2026-38346, bsc#1277375)
  * swscale/output: Fix integer overflow in alpha in yuv2rgba64_1_c_template()
    (CVE-2026-38349, bsc#1277369)
  * swscale/utils: Check *Inc
    (CVE-2026-38348, bsc#1277368)
- Drop patches fixed upstream:
  * ffmpeg-7-CVE-2026-40962.patch
- Rebase patches with quilt.
* Wed May 13 2026 Alynx Zhou <alynx.zhou@suse.com>
- Add ffmpeg-7-CVE-2026-40962.patch: Use 64bit in CENC subsample
  bounds checks. (CVE-2026-40962, bsc#1262237)
* Fri Apr  3 2026 Bjørn Lie <bjorn.lie@gmail.com>
- Disable VVC decoders/encoders by default.
* Fri Mar 20 2026 Federico Mena Quintero <federico@suse.com>
- Update suse_version macro for 1610 (jsc#PED-15827)
* Sat Jan 10 2026 Jan Engelhardt <jengelh@inai.de>
- Update to release 7.1.3
  * No release notes were provided
  * lavc/aarch64: Fix addp overflow in ff_pred16x16_plane_neon_10
  * swscale/output: Fix integer overflow in yuv2ya16_X_c_template()
  * avformat/avformat: clear FFFormatContext packet queue when
    closing a muxer
- Delete ffmpeg-7-CVE-2025-25473.patch (merged)
* Fri Sep 19 2025 Bjørn Lie <bjorn.lie@gmail.com>
- Update to version 7.1.2:
  * avcodec/librsvgdec: fix compilation with librsvg 2.50.3
  * libavfilter/af_firequalizer: Add check for av_malloc_array()
  * avcodec/libsvtav1: unbreak build with latest svtav1
  * avformat/hls: Fix Youtube AAC
  * Various bugfixes.
  * aacenc_tns: clamp filter direction energy measurement
    (CVE-2025-1594, bsc#1237561)
  * avcodec/jpeg2000dec: implement cdef remapping during pixel format matching
    (CVE-2025-9951, bsc#1249393)
  * libavfilter/af_firequalizer: Add check for av_malloc_array()
    (CVE-2025-10256, bsc#1249431)
- Drop patches fixed upstream:
  * 0001-avcodec-libsvtav1-unbreak-build-with-latest-svtav1.patch
  * ffmpeg-CVE-2025-7700.patch
* Wed Jul 23 2025 Hans-Peter Jansen <hp@urpla.net>
- Add vvenc build conditional
* Wed Jul 23 2025 SongChuan Kang <sckang@suse.com>
- Add ffmpeg-CVE-2025-7700.patch: Add check for the return value
  of av_malloc_array() and av_calloc() to avoid potential NULL
  pointer dereference(CVE-2025-7700, bsc#1246790).
* Wed Jun 25 2025 Yifan Jiang <yfjiang@suse.com>
- Built with noopenh264, drop ffmpeg-dlopen-openh264.patch
  (jsc#PED-12607)
* Thu Jun 12 2025 Jan Engelhardt <jengelh@inai.de>
- Enable libiec61883 integration [boo#1244453]
* Fri Apr  4 2025 Jan Engelhardt <jengelh@inai.de>
- Disable OpenVINO, too many dependencies for Factory ring1.
* Tue Apr  1 2025 Jan Engelhardt <jengelh@inai.de>
- Update to release 7.1.1
  * avformat/wavdec: Fix overflow of intermediate in
    block_align check
  * avformat/dvdvideodec: drop packets with unset PTS or DTS
  * avutil/timecode: Avoid fps overflow in
    av_timecode_get_smpte_from_framenum()
  * avcodec/mjpegdec: Disallow progressive bayer images
  * avformat/mov: don't unconditionally set all audio packets
    in fragments as key frames
  * avcodec/libx265: resolve build failure for
    libx265.so.n, n >= 213
  * avfilter/buffersrc: check for valid sample rate.
    (CVE-2025-22919, bsc#1237371)
  * avfilter/af_pan: Fix sscanf() use.
    (CVE-2025-0518, bsc#1236007)
  * avformat/iamf_parse: add missing constrains for num_parameters
    in audio_element_oub().
    (CVE-2025-1816, bsc#1238728)
  * avformat/hls: Be more picky on extensions.
    (CVE-2023-6602, bsc#1220546, CVE-2023-6604, bsc#1220549)
- Delete ffmpeg-7-CVE-2025-22919.patch,
  ffmpeg-7-CVE-2025-0518.patch, ffmpeg-7-CVE-2025-1816.patch
  (merged)
* Tue Mar 25 2025 Adrian Schröter <adrian@suse.de>
- Move BcntSync tag to the %%else part where the mini package gets defined
* Sun Mar 23 2025 Mia Herkt <mia@0x0.st>
- Build with OpenVINO support in libavfilter
* Sun Mar 23 2025 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2025-1816.patch:
  Backport 0526535c from upstream, add missing constrains for
  num_parameters in audio_element_oub().
  (CVE-2025-1816, bsc#1238728)
* Wed Mar  5 2025 Jan Engelhardt <jengelh@inai.de>
- Add 0001-avcodec-libsvtav1-unbreak-build-with-latest-svtav1.patch
  to build with SVT-AV1 3.0.0.
* Wed Feb 19 2025 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2025-22921.patch:
  Backport 7f9c7f98 from upstream, clear array length when
  freeing it.
  (CVE-2025-22921, bsc#1237382)
* Wed Feb 19 2025 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2025-25473.patch:
  Backport c08d3004 from upstream, clear FFFormatContext packet.
  When packet_buffer is used in mux.c, and if a muxing process fails
  at a point where packets remained in said queue.
  (CVE-2025-25473, bsc#1237351)
* Wed Feb 19 2025 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2025-0518.patch:
  Backport b5b6391d from upstream, fixes memory data leak when
  use sscanf().
  (CVE-2025-0518, bsc#1236007)
* Wed Feb 19 2025 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2025-22919.patch:
  Backport 1446e37d from upstream, check for valid sample rate
  As the sample rate <= 0 is invalid.
  (CVE-2025-22919, bsc#1237371)
* Tue Oct 15 2024 Antonio Larrosa <alarrosa@suse.com>
- Adjust bconds to build the package in SLFO without xvidcore.
* Wed Oct  2 2024 Jan Engelhardt <jengelh@inai.de>
- Update to release 7.1
  * ffmpeg CLI filtergraph chaining
  * pad_vaapi, drawbox_vaapi filters
  * vf_scale supports secondary ref input and framesync options
  * vf_scale2ref deprecated
  * removed DEC Alpha DSP and support code
  * perlin video source
  * Cropping metadata parsing and writing in Matroska and MP4/MOV
    de/muxers
  * YUV colorspace negotiation for codecs and filters, obsoleting
    the YUVJ pixel format
  * Vulkan H.264 and H.265 encoders
  * stream specifiers in fftools can now match by stream
    disposition
  * LCEVC enhancement data exporting in H.26x and MP4/ISOBMFF
  * LCEVC filter
  * avcodec/mpegvideo_enc: Add check for av_packet_new_side_data (CVE-2024-12361, bsc#1237358)
  * avformat/dump: print only the actual streams in a tile grid group (CVE-2025-22920, bsc#1237380)
  * avcodec/rkmppdec: Fix double-free on error (CVE-2024-35368, bsc#1234028)
  * avcodec/wavarc: fix signed integer overflow in block type 6/19 (CVE-2024-36619, bsc#1234023)
  * avcodec/vp9: Fix race when attaching side-data for show-existing frame (CVE-2024-36615, bsc#1234017)
  * lavc/vp9: Fix regression introduced in 0ba0585. It is possible that ff_progress_frame_await() is
    calledbut ff_progress_frame_report() isn't called when a hardware acceleration method is used, so
    a thread for vp9 decoding might get stuck.
    (CVE-2024-36615, bsc#1234017).
- Delete patches/ffmpeg-7-fix-crashes.patch,
  0001-libavcodec-arm-mlpdsp_armv5te-fix-label-format-to-wo.patch (merged)
* Mon Sep 30 2024 olaf@aepfle.de
- Fix assertion due to missing priv_data cleanup on failed VAAPI
  acceleration with 11013-avcodec-decode-clean-up-if-get_hw_frames_parameters-.patch
  (ffmpeg#11013, vlc#28811)
* Thu Sep 26 2024 Stefan Dirsch <sndirsch@suse.com>
- no longer build against libmfx; build also 15.5 against libvpl
  (boo#1230983, boo#1219494)
- dropping support for libmfx below covers:
  * libmfx: improper input validation (CVE-2023-48368, bsc#1226897)
  * libmfx: improper buffer restrictions (CVE-2023-45221, bsc#1226898)
  * libmfx: out-of-bounds read (CVE-2023-22656, bsc#1226899)
  * libmfx: out-of-bounds write (CVE-2023-47282, bsc#1226900)
  * libmfx: improper buffer restrictions (CVE-2023-47169, bsc#1226901)
  * Multiple vulnerabilities in the Intel Media SDK (libmfx1) (bsc#1226892)
  * Drop libmfx dependency from our product (jira #PED-10024)
* Wed Aug 21 2024 Jan Engelhardt <jengelh@inai.de>
- Add 0001-libavcodec-arm-mlpdsp_armv5te-fix-label-format-to-wo.patch
  to resolve build failure on armv7 [boo#1229338]
* Wed Aug  7 2024 Cliff Zhao <qzhao@suse.com>
- Update to version 7.0.2:
  * avcodec/snow: Fix off by 1 error in run_buffer
  * avcodec/utils: apply the same alignment to YUV410 as we do to YUV420 for snow
  * avformat/iamf_parse: Check for 0 samples
  * swscale: [loongarch] Fix checkasm-sw_yuv2rgb failure.
  * avcodec/aacps_tablegen_template: don't redefine CONFIG_HARDCODED_TABLES
  * avutil/hwcontext_vaapi: use the correct type for VASurfaceAttribExternalBuffers.buffers
  * avcodec/pcm-bluray/dvd: Use correct pointer types on BE
  * avcodec/pngenc: fix sBIT writing for indexed-color PNGs
  * avcodec/pngdec: use 8-bit sBIT cap for indexed PNGs per spec
  * avformat/mov: check that child boxes of trak are only present inside it
  * avformat/mov: check that sample and chunk count is 1 for HEIF
  * avcodec/videotoolboxenc: Fix bitrate doesn't work as expected
  * avdevice/dshow: Don't skip audio devices if no video device is present
  * avcodec/hdrenc: Allocate more space
  * avcodec/cfhdenc: Height of 16 is not supported
  * avcodec/cfhdenc: Allocate more space
  * avcodec/osq: fix integer overflow when applying factor
  * avcodec/osq: avoid using too large numbers for shifts and integers in update_residue_parameter()
  * avcodec/hevcdec: fix segfault on invalid film grain metadata (CVE-2024-32228, bsc#1227277)
  * avfilter/vf_tiltandshift: fix buffer offset for yuv422p input (CVE-2024-32229, bsc#1227295)
  * avcodec/mpegvideo_enc: Fix 1 line and one column images (CVE-2024-32230, bsc#1227296)
  * avcodec/pnmdec: Use 64bit for input size check (CVE-2024-7055, bsc#1229026)
  * fftools/ffmpeg_mux_init: Fix double-free on error (CVE-2024-35365, bsc#1235091)
  * avformat/dxa: Adjust order of operations around block align (CVE-2024-36613, bsc#1235092)
  * avfilter/vf_minterpolate: Check pts before division (CVE-2023-51798, bsc#1223304)
  * avfilter/vf_weave: Fix odd height handling (CVE-2023-51793, bsc#1223272)
  * avfilter/vf_gradfun: Do not overread last line (CVE-2023-50010, bsc#1223256)
  * avfilter/af_stereowiden: Check length (CVE-2023-51794, bsc#1223437)
  * avutil/hwcontext: Don't assume frames_uninit is reentrant (CVE-2024-31578, bsc#1223070)
  * avformat/avidec: Fix integer overflow iff ULONG_MAX < INT64_MAX (CVE-2024-36618, bsc#1234020)
  * avformat/cafdec: dont seek beyond 64bit (CVE-2024-36617, bsc#1234019)
  * avformat/westwood_vqa: Fix 2g packets (CVE-2024-36616, bsc#1234018)
  * avformat/sbgdec: Check for negative duration (CVE-2024-35366, bsc#1234030)
  * avcodec/ppc/vp8dsp_altivec: Fix out-of-bounds access h_subpel_filters_inner[i] and
    h_subpel_filters_outer[i / 2] belong together and the former allows the range 0..6.
    (CVE-2024-35367, bsc#1234029)
- Drop ffmpeg-7-CVE-2024-32228.patch:
  The fix has been merged.
- Drop ffmpeg-7-CVE-2024-32229.patch:
  The fix has been merged.
- Drop ffmpeg-7-CVE-2024-32230.patch:
  The fix has been merged.
* Sat Aug  3 2024 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-fix-crashes.patch:
  Backport 5b87869c from upstream, fix track handling when mixing
  IAMF and video tracks, Fixes crashes when muxing the two together.
* Fri Jul  5 2024 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2024-32229.patch:
  Backport a528a54e from upstream, Fix buffer offset for yuv422p
  input.
  (CVE-2024-32229, bsc#1227295)
* Tue Jul  2 2024 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2024-32230.patch:
  Backport 96449cfe from upstream, Fix 1 line and one column images.
  (CVE-2024-32230, bsc#1227296)
* Tue Jul  2 2024 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-7-CVE-2024-32228.patch:
  Backport 45964876 from upstream, Fix segfault on invalid film
  grain metadata.
  (CVE-2024-32228, bsc#1227277)
* Sun Apr  7 2024 Jan Engelhardt <jengelh@inai.de>
- Copy package ffmpeg-6 to ffmpeg-7 and adjust
- Update to release 7.0.0
  * Made the CLI tool support multithreading
- Delete 0001-avcodec-tests-rename-the-bundled-Mesa-AV1-vulkan-vid.patch
  (merged)
* Fri Mar 22 2024 Jan Engelhardt <jengelh@inai.de>
- Add 0001-avcodec-tests-rename-the-bundled-Mesa-AV1-vulkan-vid.patch
* Thu Mar 14 2024 Jan Engelhardt <jengelh@inai.de>
- Let the ffmpeg-6 main program be combinable with ffmpeg-6-mini-libs
* Mon Jan 15 2024 Enrico Belleri <kilgore.trout@idesmi.eu>
- Update to version 6.1.1:
  * libaribcaption decoder
  * Playdate video decoder and demuxer
  * Extend VAAPI support for libva-win32 on Windows
  * afireqsrc audio source filter
  * arls filter
  * ffmpeg CLI new option: -readrate_initial_burst
  * zoneplate video source filter
  * command support in the setpts and asetpts filters
  * Vulkan decode hwaccel, supporting H264, HEVC and AV1
  * color_vulkan filter
  * bwdif_vulkan filter
  * nlmeans_vulkan filter
  * RivaTuner video decoder
  * xfade_vulkan filter
  * vMix video decoder
  * Essential Video Coding parser, muxer and demuxer
  * Essential Video Coding frame merge bsf
  * bwdif_cuda filter
  * Microsoft RLE video encoder
  * Raw AC-4 muxer and demuxer
  * Raw VVC bitstream parser, muxer and demuxer
  * Bitstream filter for editing metadata in VVC streams
  * Bitstream filter for converting VVC from MP4 to Annex B
  * scale_vt filter for videotoolbox
  * transpose_vt filter for videotoolbox
  * support for the P_SKIP hinting to speed up libx264 encoding
  * Support HEVC,VP9,AV1 codec in enhanced flv format
  * apsnr and asisdr audio filters
  * OSQ demuxer and decoder
  * Support HEVC,VP9,AV1 codec fourcclist in enhanced rtmp protocol
  * CRI USM demuxer
  * ffmpeg CLI '-top' option deprecated in favor of the setfield filter
  * VAAPI AV1 encoder
  * ffprobe XML output schema changed to account for multiple variable-fields elements within the same parent element
  * ffprobe -output_format option added as an alias of -of
  * avformat/hls: remove non standard hls extension. (CVE-2023-6601, bsc#1220545)
- Remove patch6 0001-avfilter-vf_libplacebo-remove-deprecated-field.diff
- Prefer libvpl to libmfx: the latter is deprecated
- Delete ffmpeg-6-private-devel package as it is only needed to build libav-tools
* Wed Nov 22 2023 Bjørn Lie <bjorn.lie@gmail.com>
- Enable more decoders and encoders explicitly:
  * amrwb via bcond_without for TW only (and in
    enable_decoder/encoder)
  * opencore via bcond_without for TW only (and in
    enable_decoder/encoder)
  * xvid via bcond_without for TW only (and in
    enable_decoder/encoder)
  * h.263 via enable_decoder/encoder and no longer explicitly
    disabling in call to configure
  * MPEG4 Visual via enable_decoder/encoder and no longer
    explicitly disabling in call to configure
  * MPEG2 Hardware decoders via enable_decoder/encoder
  * And many many more via enable_decoder/encoder.
* Fri Nov 10 2023 Bjørn Lie <bjorn.lie@gmail.com>
- Update to version 6.0.1:
  * Updates and bugfixes to avcodecs, avformat and avfilters
    mainly.
- Drop patch fixed upstream:
  * 0001-avcodec-x86-mathops-clip-constants-used-with-shift-i.patch
* Wed Oct  4 2023 Manfred Hollstein <manfred.h@gmx.net>
- Add 0001-avcodec-x86-mathops-clip-constants-used-with-shift-i.patch
  to resolve a build failure on 15.4/15.5.
* Mon Jul 31 2023 llyyr <llyyr.public@gmail.com>
- Bump required libplacebo version to v6.292.0 or newer for TW
- Temporarily demote deprecation errors to deprecation warnings
  for vf_libplacebo
- Add upstream patches to fix build with libplacebo v6:
  * 0001-avfilter-vf_libplacebo-remove-deprecated-field.diff
* Mon Apr 10 2023 Jan Engelhardt <jengelh@inai.de>
- Reset fixed leftover value for BUILD_ORIG
* Thu Mar 16 2023 Jan Engelhardt <jengelh@inai.de>
- Conflict with otherproviders(ffmpeg-tools).
* Thu Mar  9 2023 Enrico Belleri <idesmi@protonmail.com>
- enable libplacebo filter
- clean old BuildRequires conditions
- add libjxl to enable_encoders
* Tue Feb 28 2023 Jan Engelhardt <jengelh@inai.de>
- Branch from ffmpeg-5.spec
- Remove ffmpeg-4.4-CVE-2020-22046.patch (inapplicable),
  no-vk-video-decoding.patch (obsolete),
  ffmpeg-CVE-2022-3964.patch (appears merged)
- Update to release 6.0
  * FFmpeg now runs every muxer in a separate thread and requires
    threading to be enabled for compilation
  * VA-API encoding and decoding support for 10/12-bit 422,
    10/12-bit 444 VP9 support
  * RISC-V optimizations
