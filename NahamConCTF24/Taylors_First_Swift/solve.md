xorEncrypt
```
__int64 __fastcall xorEncrypt(_:_:)(__int64 a1, __int64 a2)
{
  __int64 v2; // x0
  __int64 result; // x0
  __int64 v4; // x21
  __int64 v5; // x1
  __int64 v6; // x0
  __int64 v7; // [xsp+8h] [xbp-C8h]
  __int64 v8; // [xsp+10h] [xbp-C0h]
  __int64 v9; // [xsp+20h] [xbp-B0h]
  __int64 v10; // [xsp+30h] [xbp-A0h]
  __int64 v11; // [xsp+38h] [xbp-98h]
  __int64 v13; // [xsp+50h] [xbp-80h]
  __int64 v14; // [xsp+58h] [xbp-78h]
  char v15[16]; // [xsp+60h] [xbp-70h] BYREF
  __int64 v16; // [xsp+70h] [xbp-60h]
  __int64 v17; // [xsp+78h] [xbp-58h] BYREF
  __int64 v18; // [xsp+80h] [xbp-50h]
  __int64 v19[5]; // [xsp+88h] [xbp-48h] BYREF

  v18 = 0LL;
  v19[4] = a1;
  v19[3] = a2;
  v19[1] = a1;
  v10 = __swift_instantiateConcreteTypeFromMangledName(&_sSays5UInt8VGMD);
  v11 = lazy protocol witness table accessor for type [UInt8] and conformance [A]();
  Sequence.enumerated()(v10);
  v19[0] = v19[2];
  swift_bridgeObjectRetain(a2);
  v16 = a2;
  v13 = __swift_instantiateConcreteTypeFromMangledName(&_ss18EnumeratedSequenceVySays5UInt8VGGMD);
  v2 = lazy protocol witness table accessor for type EnumeratedSequence<[UInt8]> and conformance EnumeratedSequence<A>();
  result = Sequence.map<A>(_:)(partial apply for closure #1 in xorEncrypt(_:_:), v15, v13, &dword_100000014, v2);
  v14 = result;
  if ( v4 )
  {
    __break(1u);
  }
  else
  {
    swift_bridgeObjectRelease(a2);
    outlined destroy of EnumeratedSequence<[UInt8]>(v19);
    v18 = v14;
    swift_bridgeObjectRetain(v14);
    v17 = v14;
    v7 = Data.init<A>(_:)(&v17, v10, v11);
    v8 = v5;
    v6 = default argument 0 of Data.base64EncodedString(options:)();
    v9 = Data.base64EncodedString(options:)(v6, v7, v8);
    outlined consume of Data._Representation(v7, v8);
    swift_bridgeObjectRelease(v14);
    return v9;
  }
  return result;
```

flagCheck
```
__int64 __fastcall flagCheck(_:)(__int64 a1, __int64 a2)
{
  __int64 v2; // x1
  __int64 v3; // x1
  __int64 v4; // x0
  _BYTE *v5; // x1
  __int64 v6; // x1
  __int64 v7; // x1
  __int64 v8; // x0
  void *v9; // x1
  __int64 v13; // [xsp+18h] [xbp-B8h]
  __int64 v14; // [xsp+20h] [xbp-B0h]
  __int64 v15; // [xsp+28h] [xbp-A8h]
  __int64 v16; // [xsp+50h] [xbp-80h]
  __int64 v17; // [xsp+58h] [xbp-78h]
  __int64 v18; // [xsp+60h] [xbp-70h]
  __int64 v19; // [xsp+68h] [xbp-68h]
  char v20; // [xsp+74h] [xbp-5Ch]
  __int64 v21[4]; // [xsp+78h] [xbp-58h] BYREF
  __int64 v22[3]; // [xsp+98h] [xbp-38h] BYREF
  __int64 v23[4]; // [xsp+B0h] [xbp-20h] BYREF

  v23[2] = a1;
  v23[3] = a2;
  v23[0] = ((__int64 (*)(void))String.utf8.getter)();
  v23[1] = v2;
  lazy protocol witness table accessor for type String.UTF8View and conformance String.UTF8View();
  v19 = Array.init<A>(_:)(v23, &dword_100000014, &dword_100000004);
  v22[2] = v19;
  v22[0] = String.utf8.getter(a1, a2);
  v22[1] = v3;
  v14 = Array.init<A>(_:)(v22, &dword_100000014, &dword_100000004);
  v4 = _allocateUninitializedArray<A>(_:)(9LL, &dword_100000014);
  *v5 = 115;
  v5[1] = 119;
  v5[2] = 105;
  v5[3] = 102;
  v5[4] = 116;
  v5[5] = 105;
  v5[6] = 101;
  v5[7] = 115;
  v5[8] = 33;
  v13 = _finalizeUninitializedArray<A>(_:)(v4, &dword_100000014);
  v15 = xorEncrypt(_:_:)(v14, v13);
  v18 = v6;
  swift_bridgeObjectRelease(v13);
  swift_bridgeObjectRelease(v14);
  v21[2] = v15;
  v21[3] = v18;
  v21[0] = String.utf8.getter(v15, v18);
  v21[1] = v7;
  v17 = Array.init<A>(_:)(v21, &dword_100000014, &dword_100000004);
  v8 = _allocateUninitializedArray<A>(_:)(52LL, &dword_100000014);
  qmemcpy(v9, "FRsIAQ8PVBUVEREIVERbBkURFkUIBxVQVkAYFxJfV0FYVkIVQgo=", 52);
  v16 = _finalizeUninitializedArray<A>(_:)(v8, &dword_100000014);
  v20 = static Array<A>.== infix(_:_:)(v17);
  swift_bridgeObjectRelease(v16);
  swift_bridgeObjectRelease(v17);
  swift_bridgeObjectRelease(v18);
  swift_bridgeObjectRelease(v19);
  return v20 & 1;
}
```
