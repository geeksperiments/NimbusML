# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
TensorFlowScorer
"""

__all__ = ["TensorFlowScorer"]


from ...entrypoints.transforms_tensorflowscorer import \
    transforms_tensorflowscorer
from ...utils.utils import trace
from ..base_pipeline_item import BasePipelineItem, DefaultSignature


class TensorFlowScorer(BasePipelineItem, DefaultSignature):
    """

    Transforms the data using the
    `TensorFlow
    <https://www.tensorflow.org/>`_ model.

    .. remarks::
       The TensorflowTransform extracts the specified outputs
       from the operations computed on the graph (given the
       input(s)) using a pre-trained
       `TensorFlow <https://www.tensorflow.org/>`_ model.
       The transform takes as input the Tensorflow model together
       with the names of the inputs to the model and names of
       the operations for which output values will be extracted
       from the model.

       This transform has the floowing assumptions regarding the
       input, output and processing of data:

        * The transform currently accepts the
            `frozen TensorFlow model
            <https://www.tensorflow.org/mobile/prepare_models>`_
            as the input.
        * The name of input column(s) should match the name
            of input(s) in Tensorflow model.
        * The name of each output column should match one of the
            operations in the Tensorflow graph.

    :param model: TensorFlow model used by the transform. Please see
        https://www.tensorflow.org/mobile/prepare_models for more details.

    :param input_columns: The names of the model inputs.

    :param output_columns: The name of the outputs.

    :param params: Additional arguments sent to compute engine.

    .. index:: transform

    Example:
       .. literalinclude:: /../nimbusml/examples/TensorFlowScorer.py
              :language: python
    """

    @trace
    def __init__(
            self,
            model,
            input_columns=None,
            output_columns=None,
            **params):
        BasePipelineItem.__init__(
            self, type='transform', **params)

        self.model = model
        self.input_columns = input_columns
        self.output_columns = output_columns

    @property
    def _entrypoint(self):
        return transforms_tensorflowscorer

    @trace
    def _get_node(self, **all_args):
        algo_args = dict(
            model_location=self.model,
            input_columns=self.input_columns,
            output_columns=self.output_columns)

        all_args.update(algo_args)
        return self._entrypoint(**all_args)