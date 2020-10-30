# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/vision_v1p4beta1/proto/product_search.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.vision_v1p4beta1.proto import (
    geometry_pb2 as google_dot_cloud_dot_vision__v1p4beta1_dot_proto_dot_geometry__pb2,
)
from google.cloud.vision_v1p4beta1.proto import (
    product_search_service_pb2 as google_dot_cloud_dot_vision__v1p4beta1_dot_proto_dot_product__search__service__pb2,
)
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/vision_v1p4beta1/proto/product_search.proto",
    package="google.cloud.vision.v1p4beta1",
    syntax="proto3",
    serialized_options=_b(
        "\n!com.google.cloud.vision.v1p4beta1B\022ProductSearchProtoP\001ZCgoogle.golang.org/genproto/googleapis/cloud/vision/v1p4beta1;vision\370\001\001\242\002\004GCVN"
    ),
    serialized_pb=_b(
        '\n8google/cloud/vision_v1p4beta1/proto/product_search.proto\x12\x1dgoogle.cloud.vision.v1p4beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/api/resource.proto\x1a\x32google/cloud/vision_v1p4beta1/proto/geometry.proto\x1a@google/cloud/vision_v1p4beta1/proto/product_search_service.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc1\x01\n\x13ProductSearchParams\x12\x42\n\rbounding_poly\x18\t \x01(\x0b\x32+.google.cloud.vision.v1p4beta1.BoundingPoly\x12:\n\x0bproduct_set\x18\x06 \x01(\tB%\xfa\x41"\n vision.googleapis.com/ProductSet\x12\x1a\n\x12product_categories\x18\x07 \x03(\t\x12\x0e\n\x06\x66ilter\x18\x08 \x01(\t"\xb2\x05\n\x14ProductSearchResults\x12.\n\nindex_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12K\n\x07results\x18\x05 \x03(\x0b\x32:.google.cloud.vision.v1p4beta1.ProductSearchResults.Result\x12\x62\n\x17product_grouped_results\x18\x06 \x03(\x0b\x32\x41.google.cloud.vision.v1p4beta1.ProductSearchResults.GroupedResult\x1a_\n\x06Result\x12\x37\n\x07product\x18\x01 \x01(\x0b\x32&.google.cloud.vision.v1p4beta1.Product\x12\r\n\x05score\x18\x02 \x01(\x02\x12\r\n\x05image\x18\x03 \x01(\t\x1aS\n\x10ObjectAnnotation\x12\x0b\n\x03mid\x18\x01 \x01(\t\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05score\x18\x04 \x01(\x02\x1a\x82\x02\n\rGroupedResult\x12\x42\n\rbounding_poly\x18\x01 \x01(\x0b\x32+.google.cloud.vision.v1p4beta1.BoundingPoly\x12K\n\x07results\x18\x02 \x03(\x0b\x32:.google.cloud.vision.v1p4beta1.ProductSearchResults.Result\x12`\n\x12object_annotations\x18\x03 \x03(\x0b\x32\x44.google.cloud.vision.v1p4beta1.ProductSearchResults.ObjectAnnotationB\x88\x01\n!com.google.cloud.vision.v1p4beta1B\x12ProductSearchProtoP\x01ZCgoogle.golang.org/genproto/googleapis/cloud/vision/v1p4beta1;vision\xf8\x01\x01\xa2\x02\x04GCVNb\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_cloud_dot_vision__v1p4beta1_dot_proto_dot_geometry__pb2.DESCRIPTOR,
        google_dot_cloud_dot_vision__v1p4beta1_dot_proto_dot_product__search__service__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
    ],
)


_PRODUCTSEARCHPARAMS = _descriptor.Descriptor(
    name="ProductSearchParams",
    full_name="google.cloud.vision.v1p4beta1.ProductSearchParams",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="bounding_poly",
            full_name="google.cloud.vision.v1p4beta1.ProductSearchParams.bounding_poly",
            index=0,
            number=9,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="product_set",
            full_name="google.cloud.vision.v1p4beta1.ProductSearchParams.product_set",
            index=1,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b('\372A"\n vision.googleapis.com/ProductSet'),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="product_categories",
            full_name="google.cloud.vision.v1p4beta1.ProductSearchParams.product_categories",
            index=2,
            number=7,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="filter",
            full_name="google.cloud.vision.v1p4beta1.ProductSearchParams.filter",
            index=3,
            number=8,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=300,
    serialized_end=493,
)


_PRODUCTSEARCHRESULTS_RESULT = _descriptor.Descriptor(
    name="Result",
    full_name="google.cloud.vision.v1p4beta1.ProductSearchResults.Result",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="product",
            full_name="google.cloud.vision.v1p4beta1.ProductSearchResults.Result.product",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="score",
            full_name="google.cloud.vision.v1p4beta1.ProductSearchResults.Result.score",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="image",
            full_name="google.cloud.vision.v1p4beta1.ProductSearchResults.Result.image",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=745,
    serialized_end=840,
)

_PRODUCTSEARCHRESULTS_OBJECTANNOTATION = _descriptor.Descriptor(
    name="ObjectAnnotation",
    full_name="google.cloud.vision.v1p4beta1.ProductSearchResults.ObjectAnnotation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="mid",
            full_name="google.cloud.vision.v1p4beta1.ProductSearchResults.ObjectAnnotation.mid",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="language_code",
            full_name="google.cloud.vision.v1p4beta1.ProductSearchResults.ObjectAnnotation.language_code",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.vision.v1p4beta1.ProductSearchResults.ObjectAnnotation.name",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="score",
            full_name="google.cloud.vision.v1p4beta1.ProductSearchResults.ObjectAnnotation.score",
            index=3,
            number=4,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=842,
    serialized_end=925,
)

_PRODUCTSEARCHRESULTS_GROUPEDRESULT = _descriptor.Descriptor(
    name="GroupedResult",
    full_name="google.cloud.vision.v1p4beta1.ProductSearchResults.GroupedResult",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="bounding_poly",
            full_name="google.cloud.vision.v1p4beta1.ProductSearchResults.GroupedResult.bounding_poly",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="results",
            full_name="google.cloud.vision.v1p4beta1.ProductSearchResults.GroupedResult.results",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="object_annotations",
            full_name="google.cloud.vision.v1p4beta1.ProductSearchResults.GroupedResult.object_annotations",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=928,
    serialized_end=1186,
)

_PRODUCTSEARCHRESULTS = _descriptor.Descriptor(
    name="ProductSearchResults",
    full_name="google.cloud.vision.v1p4beta1.ProductSearchResults",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="index_time",
            full_name="google.cloud.vision.v1p4beta1.ProductSearchResults.index_time",
            index=0,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="results",
            full_name="google.cloud.vision.v1p4beta1.ProductSearchResults.results",
            index=1,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="product_grouped_results",
            full_name="google.cloud.vision.v1p4beta1.ProductSearchResults.product_grouped_results",
            index=2,
            number=6,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[
        _PRODUCTSEARCHRESULTS_RESULT,
        _PRODUCTSEARCHRESULTS_OBJECTANNOTATION,
        _PRODUCTSEARCHRESULTS_GROUPEDRESULT,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=496,
    serialized_end=1186,
)

_PRODUCTSEARCHPARAMS.fields_by_name[
    "bounding_poly"
].message_type = (
    google_dot_cloud_dot_vision__v1p4beta1_dot_proto_dot_geometry__pb2._BOUNDINGPOLY
)
_PRODUCTSEARCHRESULTS_RESULT.fields_by_name[
    "product"
].message_type = (
    google_dot_cloud_dot_vision__v1p4beta1_dot_proto_dot_product__search__service__pb2._PRODUCT
)
_PRODUCTSEARCHRESULTS_RESULT.containing_type = _PRODUCTSEARCHRESULTS
_PRODUCTSEARCHRESULTS_OBJECTANNOTATION.containing_type = _PRODUCTSEARCHRESULTS
_PRODUCTSEARCHRESULTS_GROUPEDRESULT.fields_by_name[
    "bounding_poly"
].message_type = (
    google_dot_cloud_dot_vision__v1p4beta1_dot_proto_dot_geometry__pb2._BOUNDINGPOLY
)
_PRODUCTSEARCHRESULTS_GROUPEDRESULT.fields_by_name[
    "results"
].message_type = _PRODUCTSEARCHRESULTS_RESULT
_PRODUCTSEARCHRESULTS_GROUPEDRESULT.fields_by_name[
    "object_annotations"
].message_type = _PRODUCTSEARCHRESULTS_OBJECTANNOTATION
_PRODUCTSEARCHRESULTS_GROUPEDRESULT.containing_type = _PRODUCTSEARCHRESULTS
_PRODUCTSEARCHRESULTS.fields_by_name[
    "index_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PRODUCTSEARCHRESULTS.fields_by_name[
    "results"
].message_type = _PRODUCTSEARCHRESULTS_RESULT
_PRODUCTSEARCHRESULTS.fields_by_name[
    "product_grouped_results"
].message_type = _PRODUCTSEARCHRESULTS_GROUPEDRESULT
DESCRIPTOR.message_types_by_name["ProductSearchParams"] = _PRODUCTSEARCHPARAMS
DESCRIPTOR.message_types_by_name["ProductSearchResults"] = _PRODUCTSEARCHRESULTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProductSearchParams = _reflection.GeneratedProtocolMessageType(
    "ProductSearchParams",
    (_message.Message,),
    dict(
        DESCRIPTOR=_PRODUCTSEARCHPARAMS,
        __module__="google.cloud.vision_v1p4beta1.proto.product_search_pb2",
        __doc__="""Parameters for a product search request.
  
  
  Attributes:
      bounding_poly:
          The bounding polygon around the area of interest in the image.
          If it is not specified, system discretion will be applied.
      product_set:
          The resource name of a
          [ProductSet][google.cloud.vision.v1p4beta1.ProductSet] to be
          searched for similar images.  Format is: ``projects/PROJECT_ID
          /locations/LOC_ID/productSets/PRODUCT_SET_ID``.
      product_categories:
          The list of product categories to search in. Currently, we
          only consider the first category, and either "homegoods-v2",
          "apparel-v2", "toys-v2", "packagedgoods-v1", or "general-v1"
          should be specified. The legacy categories "homegoods",
          "apparel", and "toys" are still supported but will be
          deprecated. For new products, please use "homegoods-v2",
          "apparel-v2", or "toys-v2" for better product search accuracy.
          It is recommended to migrate existing products to these
          categories as well.
      filter:
          The filtering expression. This can be used to restrict search
          results based on Product labels. We currently support an AND
          of OR of key-value expressions, where each expression within
          an OR must have the same key. An '=' should be used to connect
          the key and value.  For example, "(color = red OR color =
          blue) AND brand = Google" is acceptable, but "(color = red OR
          brand = Google)" is not acceptable. "color: red" is not
          acceptable because it uses a ':' instead of an '='.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.vision.v1p4beta1.ProductSearchParams)
    ),
)
_sym_db.RegisterMessage(ProductSearchParams)

ProductSearchResults = _reflection.GeneratedProtocolMessageType(
    "ProductSearchResults",
    (_message.Message,),
    dict(
        Result=_reflection.GeneratedProtocolMessageType(
            "Result",
            (_message.Message,),
            dict(
                DESCRIPTOR=_PRODUCTSEARCHRESULTS_RESULT,
                __module__="google.cloud.vision_v1p4beta1.proto.product_search_pb2",
                __doc__="""Information about a product.
    
    
    Attributes:
        product:
            The Product.
        score:
            A confidence level on the match, ranging from 0 (no
            confidence) to 1 (full confidence).
        image:
            The resource name of the image from the product that is the
            closest match to the query.
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.vision.v1p4beta1.ProductSearchResults.Result)
            ),
        ),
        ObjectAnnotation=_reflection.GeneratedProtocolMessageType(
            "ObjectAnnotation",
            (_message.Message,),
            dict(
                DESCRIPTOR=_PRODUCTSEARCHRESULTS_OBJECTANNOTATION,
                __module__="google.cloud.vision_v1p4beta1.proto.product_search_pb2",
                __doc__="""Prediction for what the object in the bounding box is.
    
    
    Attributes:
        mid:
            Object ID that should align with EntityAnnotation mid.
        language_code:
            The BCP-47 language code, such as "en-US" or "sr-Latn". For
            more information, see http://www.unicode.org/reports/tr35/#Uni
            code\_locale\_identifier.
        name:
            Object name, expressed in its ``language_code`` language.
        score:
            Score of the result. Range [0, 1].
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.vision.v1p4beta1.ProductSearchResults.ObjectAnnotation)
            ),
        ),
        GroupedResult=_reflection.GeneratedProtocolMessageType(
            "GroupedResult",
            (_message.Message,),
            dict(
                DESCRIPTOR=_PRODUCTSEARCHRESULTS_GROUPEDRESULT,
                __module__="google.cloud.vision_v1p4beta1.proto.product_search_pb2",
                __doc__="""Information about the products similar to a single product
    in a query image.
    
    
    Attributes:
        bounding_poly:
            The bounding polygon around the product detected in the query
            image.
        results:
            List of results, one for each product match.
        object_annotations:
            List of generic predictions for the object in the bounding
            box.
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.vision.v1p4beta1.ProductSearchResults.GroupedResult)
            ),
        ),
        DESCRIPTOR=_PRODUCTSEARCHRESULTS,
        __module__="google.cloud.vision_v1p4beta1.proto.product_search_pb2",
        __doc__="""Results for a product search request.
  
  
  Attributes:
      index_time:
          Timestamp of the index which provided these results. Products
          added to the product set and products removed from the product
          set after this time are not reflected in the current results.
      results:
          List of results, one for each product match.
      product_grouped_results:
          List of results grouped by products detected in the query
          image. Each entry corresponds to one bounding polygon in the
          query image, and contains the matching products specific to
          that region. There may be duplicate product matches in the
          union of all the per-product results.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.vision.v1p4beta1.ProductSearchResults)
    ),
)
_sym_db.RegisterMessage(ProductSearchResults)
_sym_db.RegisterMessage(ProductSearchResults.Result)
_sym_db.RegisterMessage(ProductSearchResults.ObjectAnnotation)
_sym_db.RegisterMessage(ProductSearchResults.GroupedResult)


DESCRIPTOR._options = None
_PRODUCTSEARCHPARAMS.fields_by_name["product_set"]._options = None
# @@protoc_insertion_point(module_scope)
