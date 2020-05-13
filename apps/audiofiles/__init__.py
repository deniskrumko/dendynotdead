# Audio file formats
# ============================================================================

AUDIO_MP3 = 'mp3'
AUDIO_OGG = 'ogg'
AUDIO_WAV = 'wav'

AUDIO_FORMATS = (
    (AUDIO_MP3, 'mp3 format'),
    (AUDIO_OGG, 'ogg format'),
    (AUDIO_WAV, 'wav format'),
)

# Audio MIME types
# ============================================================================

AUDIO_MIMETYPES = {
    AUDIO_MP3: 'audio/mpeg',
    AUDIO_OGG: 'audio/ogg',
    AUDIO_WAV: 'audio/wav',
}

# Audio types
# ============================================================================

AUDIO_GTP = 'gtp'
AUDIO_RECORDED = 'rec'
AUDIO_DEMO = 'dem'
AUDIO_ACOUSTIC = 'aco'
AUDIO_INSTRUMENTAL = 'ins'
AUDIO_LIVE = 'liv'
AUDIO_OTHER = 'oth'

AUDIO_VERSION = (
    (AUDIO_GTP, 'GuitarPro version'),
    (AUDIO_RECORDED, 'Recorded version'),
    (AUDIO_DEMO, 'Demo version'),
    (AUDIO_ACOUSTIC, 'Acoustic version'),
    (AUDIO_INSTRUMENTAL, 'Instrumental version'),
    (AUDIO_LIVE, 'Live version'),
    (AUDIO_OTHER, 'Other version')
)

# Artists
# ============================================================================

DND = 'Dendy Not Dead'
DK = 'Deniska Krumko'
