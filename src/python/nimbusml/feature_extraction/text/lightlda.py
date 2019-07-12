# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
LightLda
"""

__all__ = ["LightLda"]


from sklearn.base import TransformerMixin

from ...base_transform import BaseTransform
from ...internal.core.feature_extraction.text.lightlda import LightLda as core
from ...internal.utils.utils import trace


class LightLda(core, BaseTransform, TransformerMixin):
    """

    The LDA transform implements LightLDA, a state-of-the-art
    implementation of Latent Dirichlet Allocation.

    .. remarks::
        Latent Dirichlet Allocation is a well-known topic modeling algorithm
        that infers topical structure from text
        data, and can be used to featurize any text fields as low-dimensional
        topical vectors. LightLDA is an extremely
        efficient implementation of LDA developed in MSR-Asia that
        incorporates a number of optimization techniques
        `(http://arxiv.org/abs/1412.1576) <http://arxiv.org/abs/1412.1576>`_.
        With the LDA transform, we can
        train a topic model to produce 1 million topics with 1 million
        vocabulary on a 1-billion-token document set one
        a single machine in a few hours (typically, LDA at this scale takes
        days and requires large clusters). The most
        significant innovation is a super-efficient O(1) Metropolis-Hastings
        sampling algorithm, whose running cost is
        (surprisingly) agnostic of model size, allowing it to converges
        nearly an order of magnitude faster than other
        Gibbs samplers.


    :param columns: see `Columns </nimbusml/concepts/columns>`_.

    :param num_topic: The number of topics.

    :param number_of_threads: The number of training threads. Default value
        depends on number of logical processors.

    :param num_max_doc_token: The threshold of maximum count of tokens per doc.

    :param alpha_sum: Dirichlet prior on document-topic vectors.

    :param beta: Dirichlet prior on vocab-topic vectors.

    :param mhstep: Number of Metropolis Hasting step.

    :param num_iterations: Number of iterations.

    :param likelihood_interval: Compute log likelihood over local dataset on
        this iteration interval.

    :param num_summary_term_per_topic: The number of words to summarize the
        topic.

    :param num_burnin_iterations: The number of burn-in iterations.

    :param reset_random_generator: Reset the random number generator for each
        document.

    :param output_topic_word_summary: Whether to output the topic-word summary
        in text format.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:class:`NGramFeaturizer
        <nimbusml.feature_extraction.text.NGramFeaturizer>`,
        :py:class:`Sentiment
        <nimbusml.feature_extraction.text.Sentiment>`,
        :py:class:`WordEmbedding
        <nimbusml.feature_extraction.text.WordEmbedding>`.

    .. index:: transform, featurizer, text

    Example:
       .. literalinclude:: /../nimbusml/examples/LightLda.py
              :language: python
    """

    @trace
    def __init__(
            self,
            num_topic=100,
            number_of_threads=0,
            num_max_doc_token=512,
            alpha_sum=100.0,
            beta=0.01,
            mhstep=4,
            num_iterations=200,
            likelihood_interval=5,
            num_summary_term_per_topic=10,
            num_burnin_iterations=10,
            reset_random_generator=False,
            output_topic_word_summary=False,
            columns=None,
            **params):

        if columns:
            params['columns'] = columns
        BaseTransform.__init__(self, **params)
        core.__init__(
            self,
            num_topic=num_topic,
            number_of_threads=number_of_threads,
            num_max_doc_token=num_max_doc_token,
            alpha_sum=alpha_sum,
            beta=beta,
            mhstep=mhstep,
            num_iterations=num_iterations,
            likelihood_interval=likelihood_interval,
            num_summary_term_per_topic=num_summary_term_per_topic,
            num_burnin_iterations=num_burnin_iterations,
            reset_random_generator=reset_random_generator,
            output_topic_word_summary=output_topic_word_summary,
            **params)
        self._columns = columns

    def get_params(self, deep=False):
        """
        Get the parameters for this operator.
        """
        return core.get_params(self)