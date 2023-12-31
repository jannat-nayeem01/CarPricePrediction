from _typeshed import Incomplete, SupportsKeysAndGetItem
from collections.abc import Iterable
from typing import Any, NoReturn
from typing_extensions import Final, Literal, Self, TypeAlias

from .util import AbstractKeystore, AbstractKeystoreEntry

__version_info__: Final[tuple[int, int, int] | tuple[int, int, int, str]]
__version__: Final[str]
MAGIC_NUMBER_JKS: Final[bytes]
MAGIC_NUMBER_JCEKS: Final[bytes]
SIGNATURE_WHITENING: Final[bytes]

_JksType: TypeAlias = Literal["jks", "jceks"]
_CertType: TypeAlias = Literal["X.509"]
_KeyFormat: TypeAlias = Literal["pkcs8", "rsa_raw"]

class TrustedCertEntry(AbstractKeystoreEntry):
    store_type: _JksType | None
    type: _CertType | None
    cert: bytes
    def __init__(
        self,
        *,
        type: _CertType = ...,
        cert: bytes = ...,
        store_type: _JksType = ...,
        alias: str = ...,
        timestamp: int = ...,
        **kwargs: Any,
    ) -> None: ...
    @classmethod
    def new(cls, alias: str, cert: bytes) -> Self: ...  # type: ignore[override]
    def is_decrypted(self) -> Literal[True]: ...

class PrivateKeyEntry(AbstractKeystoreEntry):
    store_type: _JksType | None
    cert_chain: list[tuple[_CertType, bytes]]
    # Properties provided by __getattr__ after decryption
    @property
    def pkey(self) -> bytes: ...
    @property
    def pkey_pkcs8(self) -> bytes: ...
    @property
    def algorithm_oid(self) -> tuple[int, ...]: ...
    def __init__(
        self,
        *,
        cert_chain: list[tuple[_CertType, bytes]] = ...,
        encrypted: bool = ...,
        pkey: bytes = ...,
        pkey_pkcs8: bytes = ...,
        algorithm_oid: tuple[int, ...] = ...,
        store_type: _JksType = ...,
        alias: str = ...,
        timestamp: int = ...,
        **kwargs: Any,
    ) -> None: ...
    @classmethod
    def new(  # type: ignore[override]
        cls, alias: str, certs: Iterable[bytes], key: bytes, key_format: _KeyFormat = "pkcs8"
    ) -> Self: ...

class SecretKeyEntry(AbstractKeystoreEntry):
    store_type: _JksType | None
    # Properties provided by __getattr__
    @property
    def algorithm(self) -> str: ...
    @property
    def key(self) -> bytes: ...
    @property
    def key_size(self) -> int: ...
    def __init__(
        self,
        *,
        sealed_obj: Incomplete = ...,
        algorithm: str = ...,
        key: bytes = ...,
        key_size: int = ...,
        store_type: _JksType = ...,
        alias: str = ...,
        timestamp: int = ...,
        **kwargs: Any,
    ) -> None: ...
    # Not implemented by pyjks
    @classmethod
    def new(  # type: ignore[override]
        cls, alias: str, sealed_obj: bool, algorithm: str, key: bytes, key_size: int
    ) -> NoReturn: ...
    # Not implemented by pyjks
    def encrypt(self, key_password: str) -> NoReturn: ...

class KeyStore(AbstractKeystore):
    entries: dict[str, TrustedCertEntry | PrivateKeyEntry | SecretKeyEntry]  # type: ignore[assignment]
    store_type: _JksType
    @classmethod
    def new(cls, store_type: _JksType, store_entries: Iterable[TrustedCertEntry | PrivateKeyEntry | SecretKeyEntry]) -> Self: ...
    @classmethod
    def loads(cls, data: bytes, store_password: str | None, try_decrypt_keys: bool = True) -> Self: ...
    def saves(self, store_password: str) -> bytes: ...
    def __init__(
        self, store_type: _JksType, entries: SupportsKeysAndGetItem[str, TrustedCertEntry | PrivateKeyEntry | SecretKeyEntry]
    ) -> None: ...
    @property
    def certs(self) -> dict[str, TrustedCertEntry]: ...
    @property
    def secret_keys(self) -> dict[str, SecretKeyEntry]: ...
    @property
    def private_keys(self) -> dict[str, PrivateKeyEntry]: ...
