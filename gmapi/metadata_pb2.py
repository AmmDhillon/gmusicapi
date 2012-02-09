# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='metadata.proto',
  package='',
  serialized_pb='\n\x0emetadata.proto\"\xa3\x03\n\x05Track\x12\n\n\x02id\x18\x02 \x01(\t\x12\x10\n\x08\x63reation\x18\x03 \x01(\x05\x12\x12\n\nlastPlayed\x18\x04 \x01(\x05\x12\r\n\x05title\x18\x06 \x01(\t\x12\x0e\n\x06\x61rtist\x18\x07 \x01(\t\x12\x10\n\x08\x63omposer\x18\x08 \x01(\t\x12\r\n\x05\x61lbum\x18\t \x01(\t\x12\x13\n\x0b\x61lbumArtist\x18\n \x01(\t\x12\x0c\n\x04year\x18\x0b \x01(\x05\x12\x0f\n\x07\x63omment\x18\x0c \x01(\t\x12\r\n\x05track\x18\r \x01(\x05\x12\r\n\x05genre\x18\x0e \x01(\t\x12\x10\n\x08\x64uration\x18\x0f \x01(\x05\x12\x16\n\x0e\x62\x65\x61tsPerMinute\x18\x10 \x01(\x05\x12\x11\n\tplayCount\x18\x14 \x01(\x05\x12\x13\n\x0btotalTracks\x18\x1a \x01(\x05\x12\x0c\n\x04\x64isc\x18\x1b \x01(\x05\x12\x12\n\ntotalDiscs\x18\x1c \x01(\x05\x12\x0b\n\x03u11\x18\x1f \x01(\x05\x12\x10\n\x08\x66ileSize\x18  \x01(\x05\x12\x0b\n\x03u13\x18% \x01(\x05\x12\x0b\n\x03u14\x18& \x01(\x05\x12\x0f\n\x07\x62itrate\x18, \x01(\x05\x12\x0b\n\x03u15\x18\x35 \x01(\t\x12\x0b\n\x03u16\x18= \x01(\x05\":\n\x0fMetadataRequest\x12\x16\n\x06tracks\x18\x01 \x03(\x0b\x32\x06.Track\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\"8\n\x0cQueuedUpload\x12\n\n\x02id\x18\x01 \x01(\t\x12\n\n\x02u0\x18\x02 \x01(\x05\x12\x10\n\x08serverId\x18\x03 \x01(\t\"P\n\x06Status\x12\n\n\x02u0\x18\x01 \x01(\x05\x12\n\n\x02u1\x18\x02 \x01(\x05\x12\n\n\x02u2\x18\x03 \x01(\x05\x12\n\n\x02u3\x18\x04 \x01(\x05\x12\n\n\x02u4\x18\x05 \x01(\x05\x12\n\n\x02u5\x18\x06 \x01(\x05\"<\n\rTrackResponse\x12\x0b\n\x03ids\x18\x02 \x03(\t\x12\x1e\n\x07uploads\x18\x03 \x03(\x0b\x32\r.QueuedUpload\"X\n\x10MetadataResponse\x12\n\n\x02u0\x18\x01 \x01(\x05\x12 \n\x08response\x18\x02 \x01(\x0b\x32\x0e.TrackResponse\x12\x16\n\x05state\x18\x06 \x01(\x0b\x32\x07.Status\"/\n\nUploadAuth\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x10\n\x08hostname\x18\x02 \x01(\t\"L\n\x05Quota\x12\x15\n\rmaximumTracks\x18\x01 \x01(\x05\x12\x13\n\x0btotalTracks\x18\x02 \x01(\x05\x12\x17\n\x0f\x61vailableTracks\x18\x03 \x01(\x05\"\x1e\n\x0b\x43lientState\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"Q\n\x13\x43lientStateResponse\x12\n\n\x02u0\x18\x01 \x01(\x05\x12\x17\n\x06status\x18\x06 \x01(\x0b\x32\x07.Status\x12\x15\n\x05quota\x18\x08 \x01(\x0b\x32\x06.Quota\"Q\n\x12UploadAuthResponse\x12\n\n\x02u0\x18\x01 \x01(\x05\x12\x17\n\x06status\x18\x06 \x01(\x0b\x32\x07.Status\x12\n\n\x02u1\x18\x0b \x01(\x05\x12\n\n\x02u2\x18\x0c \x01(\x05')




_TRACK = descriptor.Descriptor(
  name='Track',
  full_name='Track',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='Track.id', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='creation', full_name='Track.creation', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='lastPlayed', full_name='Track.lastPlayed', index=2,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='title', full_name='Track.title', index=3,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='artist', full_name='Track.artist', index=4,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='composer', full_name='Track.composer', index=5,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='album', full_name='Track.album', index=6,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='albumArtist', full_name='Track.albumArtist', index=7,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='year', full_name='Track.year', index=8,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='comment', full_name='Track.comment', index=9,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='track', full_name='Track.track', index=10,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='genre', full_name='Track.genre', index=11,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='duration', full_name='Track.duration', index=12,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='beatsPerMinute', full_name='Track.beatsPerMinute', index=13,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='playCount', full_name='Track.playCount', index=14,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='totalTracks', full_name='Track.totalTracks', index=15,
      number=26, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='disc', full_name='Track.disc', index=16,
      number=27, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='totalDiscs', full_name='Track.totalDiscs', index=17,
      number=28, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='u11', full_name='Track.u11', index=18,
      number=31, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='fileSize', full_name='Track.fileSize', index=19,
      number=32, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='u13', full_name='Track.u13', index=20,
      number=37, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='u14', full_name='Track.u14', index=21,
      number=38, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bitrate', full_name='Track.bitrate', index=22,
      number=44, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='u15', full_name='Track.u15', index=23,
      number=53, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='u16', full_name='Track.u16', index=24,
      number=61, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=19,
  serialized_end=438,
)


_METADATAREQUEST = descriptor.Descriptor(
  name='MetadataRequest',
  full_name='MetadataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='tracks', full_name='MetadataRequest.tracks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='address', full_name='MetadataRequest.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=440,
  serialized_end=498,
)


_QUEUEDUPLOAD = descriptor.Descriptor(
  name='QueuedUpload',
  full_name='QueuedUpload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='QueuedUpload.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='u0', full_name='QueuedUpload.u0', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='serverId', full_name='QueuedUpload.serverId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=500,
  serialized_end=556,
)


_STATUS = descriptor.Descriptor(
  name='Status',
  full_name='Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='u0', full_name='Status.u0', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='u1', full_name='Status.u1', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='u2', full_name='Status.u2', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='u3', full_name='Status.u3', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='u4', full_name='Status.u4', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='u5', full_name='Status.u5', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=558,
  serialized_end=638,
)


_TRACKRESPONSE = descriptor.Descriptor(
  name='TrackResponse',
  full_name='TrackResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ids', full_name='TrackResponse.ids', index=0,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='uploads', full_name='TrackResponse.uploads', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=640,
  serialized_end=700,
)


_METADATARESPONSE = descriptor.Descriptor(
  name='MetadataResponse',
  full_name='MetadataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='u0', full_name='MetadataResponse.u0', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='response', full_name='MetadataResponse.response', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='state', full_name='MetadataResponse.state', index=2,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=702,
  serialized_end=790,
)


_UPLOADAUTH = descriptor.Descriptor(
  name='UploadAuth',
  full_name='UploadAuth',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='address', full_name='UploadAuth.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hostname', full_name='UploadAuth.hostname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=792,
  serialized_end=839,
)


_QUOTA = descriptor.Descriptor(
  name='Quota',
  full_name='Quota',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='maximumTracks', full_name='Quota.maximumTracks', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='totalTracks', full_name='Quota.totalTracks', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='availableTracks', full_name='Quota.availableTracks', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=841,
  serialized_end=917,
)


_CLIENTSTATE = descriptor.Descriptor(
  name='ClientState',
  full_name='ClientState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='address', full_name='ClientState.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=919,
  serialized_end=949,
)


_CLIENTSTATERESPONSE = descriptor.Descriptor(
  name='ClientStateResponse',
  full_name='ClientStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='u0', full_name='ClientStateResponse.u0', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='status', full_name='ClientStateResponse.status', index=1,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='quota', full_name='ClientStateResponse.quota', index=2,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=951,
  serialized_end=1032,
)


_UPLOADAUTHRESPONSE = descriptor.Descriptor(
  name='UploadAuthResponse',
  full_name='UploadAuthResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='u0', full_name='UploadAuthResponse.u0', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='status', full_name='UploadAuthResponse.status', index=1,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='u1', full_name='UploadAuthResponse.u1', index=2,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='u2', full_name='UploadAuthResponse.u2', index=3,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1034,
  serialized_end=1115,
)


_METADATAREQUEST.fields_by_name['tracks'].message_type = _TRACK
_TRACKRESPONSE.fields_by_name['uploads'].message_type = _QUEUEDUPLOAD
_METADATARESPONSE.fields_by_name['response'].message_type = _TRACKRESPONSE
_METADATARESPONSE.fields_by_name['state'].message_type = _STATUS
_CLIENTSTATERESPONSE.fields_by_name['status'].message_type = _STATUS
_CLIENTSTATERESPONSE.fields_by_name['quota'].message_type = _QUOTA
_UPLOADAUTHRESPONSE.fields_by_name['status'].message_type = _STATUS

class Track(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRACK
  
  # @@protoc_insertion_point(class_scope:Track)

class MetadataRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _METADATAREQUEST
  
  # @@protoc_insertion_point(class_scope:MetadataRequest)

class QueuedUpload(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUEUEDUPLOAD
  
  # @@protoc_insertion_point(class_scope:QueuedUpload)

class Status(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STATUS
  
  # @@protoc_insertion_point(class_scope:Status)

class TrackResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRACKRESPONSE
  
  # @@protoc_insertion_point(class_scope:TrackResponse)

class MetadataResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _METADATARESPONSE
  
  # @@protoc_insertion_point(class_scope:MetadataResponse)

class UploadAuth(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UPLOADAUTH
  
  # @@protoc_insertion_point(class_scope:UploadAuth)

class Quota(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUOTA
  
  # @@protoc_insertion_point(class_scope:Quota)

class ClientState(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CLIENTSTATE
  
  # @@protoc_insertion_point(class_scope:ClientState)

class ClientStateResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CLIENTSTATERESPONSE
  
  # @@protoc_insertion_point(class_scope:ClientStateResponse)

class UploadAuthResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UPLOADAUTHRESPONSE
  
  # @@protoc_insertion_point(class_scope:UploadAuthResponse)

# @@protoc_insertion_point(module_scope)
