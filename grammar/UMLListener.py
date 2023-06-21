# Generated from grammar/UML.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .UMLParser import UMLParser
else:
    from UMLParser import UMLParser

from diagrams.UMLImage import UMLImage
from diagrams.Diagram import Diagram
from diagrams.classes.UMLCLass import *
from diagrams.classes.UMLRelation import *
from diagrams.classes.ClassDiagram import *
from diagrams.sequence.SequenceDiagram import *
from diagrams.usecase.UseCaseDiagram import *

# This class defines a complete listener for a parse tree produced by UMLParser.


class UMLListener(ParseTreeListener):
    image: UMLImage

    # Enter a parse tree produced by UMLParser#program.
    def enterProgram(self, ctx: UMLParser.ProgramContext):
        pass

    # Exit a parse tree produced by UMLParser#program.
    def exitProgram(self, ctx: UMLParser.ProgramContext):
        self.image.draw()

    # Enter a parse tree produced by UMLParser#classDiagram.
    def enterClassDiagram(self, ctx: UMLParser.ClassDiagramContext):
        self.image = UMLImage(ClassDiagram(ctx.IDENTIFIER()))

    # Exit a parse tree produced by UMLParser#classDiagram.
    def exitClassDiagram(self, ctx: UMLParser.ClassDiagramContext):
        pass

    # Enter a parse tree produced by UMLParser#class.
    def enterClass(self, ctx: UMLParser.ClassContext):
        name = ctx.IDENTIFIER().getText()

        if self.image.diagram.get_class_by_name(name) is not None:
            raise Exception("Class with name " + name + " already exists")

        self.image.diagram.add_class(UMLBasicClass(name))

    # Exit a parse tree produced by UMLParser#class.
    def exitClass(self, ctx: UMLParser.ClassContext):
        pass

    # Enter a parse tree produced by UMLParser#interface.
    def enterInterface(self, ctx: UMLParser.InterfaceContext):
        name = ctx.IDENTIFIER().getText()

        if self.image.diagram.get_class_by_name(name) is not None:
            raise Exception("Class with name " + name + " already exists")

        self.image.diagram.add_class(UMLInterface(name))

    # Exit a parse tree produced by UMLParser#interface.
    def exitInterface(self, ctx: UMLParser.InterfaceContext):
        pass

    # Enter a parse tree produced by UMLParser#abstractClass.
    def enterAbstractClass(self, ctx: UMLParser.AbstractClassContext):
        name = ctx.IDENTIFIER().getText()

        if self.image.diagram.get_class_by_name(name) is not None:
            raise Exception("Class with name " + name + " already exists")

        self.image.diagram.add_class(UMLAbstractClass(name))

    # Exit a parse tree produced by UMLParser#abstractClass.
    def exitAbstractClass(self, ctx: UMLParser.AbstractClassContext):
        pass

    # Enter a parse tree produced by UMLParser#enum.
    def enterEnum(self, ctx: UMLParser.EnumContext):
        name = ctx.IDENTIFIER().getText()

        if self.image.diagram.get_class_by_name(name) is not None:
            raise Exception("Class with name " + name + " already exists")

        self.image.diagram.add_class(UMLEnum(name))

    # Exit a parse tree produced by UMLParser#enum.
    def exitEnum(self, ctx: UMLParser.EnumContext):
        pass

    # Enter a parse tree produced by UMLParser#classContents.
    def enterClassContents(self, ctx: UMLParser.ClassContentsContext):
        pass

    # Exit a parse tree produced by UMLParser#classContents.
    def exitClassContents(self, ctx: UMLParser.ClassContentsContext):
        pass

    # Enter a parse tree produced by UMLParser#field.
    def enterField(self, ctx: UMLParser.FieldContext):
        self.image.diagram.get_last_class().add_field(
            UMLClassField(ctx.IDENTIFIER(), ctx.SCOPE(),
                          ctx.type_().IDENTIFIER())
        )

    # Exit a parse tree produced by UMLParser#field.
    def exitField(self, ctx: UMLParser.FieldContext):
        pass

    # Enter a parse tree produced by UMLParser#type.
    def enterType(self, ctx: UMLParser.TypeContext):
        pass

    # Exit a parse tree produced by UMLParser#type.
    def exitType(self, ctx: UMLParser.TypeContext):
        pass

    # Enter a parse tree produced by UMLParser#method.
    def enterMethod(self, ctx: UMLParser.MethodContext):
        self.image.diagram.get_last_class().add_method(
            UMLClassMethod(ctx.IDENTIFIER(), ctx.SCOPE(),
                           ctx.type_().IDENTIFIER())
        )

    # Exit a parse tree produced by UMLParser#method.
    def exitMethod(self, ctx: UMLParser.MethodContext):
        pass

    # Enter a parse tree produced by UMLParser#arguments.
    def enterArguments(self, ctx: UMLParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by UMLParser#arguments.
    def exitArguments(self, ctx: UMLParser.ArgumentsContext):
        pass

    # Enter a parse tree produced by UMLParser#argument.
    def enterArgument(self, ctx: UMLParser.ArgumentContext):
        pass

    # Exit a parse tree produced by UMLParser#argument.
    def exitArgument(self, ctx: UMLParser.ArgumentContext):
        pass

    # Enter a parse tree produced by UMLParser#enumContents.
    def enterEnumContents(self, ctx: UMLParser.EnumContentsContext):
        pass

    # Exit a parse tree produced by UMLParser#enumContents.
    def exitEnumContents(self, ctx: UMLParser.EnumContentsContext):
        pass

    # Enter a parse tree produced by UMLParser#enumField.
    def enterEnumField(self, ctx: UMLParser.EnumFieldContext):
        self.image.diagram.get_last_class().add_field(
            UMLEnumField(ctx.IDENTIFIER())
        )

    # Exit a parse tree produced by UMLParser#enumField.
    def exitEnumField(self, ctx: UMLParser.EnumFieldContext):
        pass

    # Enter a parse tree produced by UMLParser#relationship.
    def enterRelationship(self, ctx: UMLParser.RelationshipContext):
        type_ = ""
        inverted = False
        target_name = ""
        if ctx.objectRelationship():
            # bez uwzgledniania krotnosci
            relation_text = ctx.objectRelationship().getText()
            # TODO: zmiana tego ifa (ewentualne rozważenie zmiany tokenu z '--' na '---')
            # if relation_text[:2] == "--" and relation_text[3]!="*":
            #     type_ = "association"
            #     target_name = relation_text[2:]
            # else:
            target_name = relation_text[3:]
            match ctx.objectRelationship().getText()[:3]:
                case "...":
                    type_ = "dependency"
                case "--o":
                    type_ = "partial_aggregation"
                case "o--":
                    type_ = "partial_aggregation"
                    inverted = True
                case "--*":
                    type_ = "full_aggregation"
                case "*--":
                    type_ = "full_aggregation"
                    inverted = True
                case _:
                    type_ = "association"
                    target_name = relation_text[2:]
        else:
            target_name = ctx.inheritance().getText()[3:]
            if ctx.inheritance().getText()[:3] == "<--":
                inverted = True
            type_ = "inheritance"

        if str(ctx.IDENTIFIER()) == target_name:
            raise Exception(f"Class {target_name} cannot be related to itself")

        if self.image.diagram.get_class_by_name(target_name) is None:
            raise Exception(f"Class {target_name} does not exist")

        if self.image.diagram.get_class_by_name(str(ctx.IDENTIFIER())) is None:
            raise Exception(f"Class {str(ctx.IDENTIFIER())} does not exist")

        source = self.image.diagram.get_class_by_name(str(ctx.IDENTIFIER()))
        target = self.image.diagram.get_class_by_name(str(target_name))
        self.image.diagram.add_relation(
            UMLRelation(
                source,
                target,
                type_,
                inverted
            )
        )

    # Exit a parse tree produced by UMLParser#relationship.
    def exitRelationship(self, ctx: UMLParser.RelationshipContext):
        pass

    # Enter a parse tree produced by UMLParser#objectRelationship.
    def enterObjectRelationship(self, ctx: UMLParser.ObjectRelationshipContext):
        # relation = self.image.diagram.get_last_relation()
        # source = relation.source
        # target_name = str(ctx.IDENTIFIER())
        # source_multiplicity = ""
        # target_multiplicity = ""
        # type_ = relation.type_
        # inverted = relation.inverted

        # target = self.image.diagram.get_class_by_name(target_name)

        # self.image.diagram.add_relation(
        #     UMLRelation(
        #     source,
        #     target,
        #     type_,
        #     inverted
        #     )
        # )
        pass

        # TODO: set multiplicity, type

    # Exit a parse tree produced by UMLParser#objectRelationship.

    def exitObjectRelationship(self, ctx: UMLParser.ObjectRelationshipContext):
        pass

    # Enter a parse tree produced by UMLParser#inheritance.
    def enterInheritance(self, ctx: UMLParser.InheritanceContext):
        # TODO: set target, multiplicity, type
        pass

    # Exit a parse tree produced by UMLParser#inheritance.
    def exitInheritance(self, ctx: UMLParser.InheritanceContext):
        pass

    # Enter a parse tree produced by UMLParser#multiplicity.
    def enterMultiplicity(self, ctx: UMLParser.MultiplicityContext):
        pass

    # Exit a parse tree produced by UMLParser#multiplicity.
    def exitMultiplicity(self, ctx: UMLParser.MultiplicityContext):
        pass

    # Enter a parse tree produced by UMLParser#useCaseDiagram.
    def enterUseCaseDiagram(self, ctx: UMLParser.UseCaseDiagramContext):
        self.image = UMLImage(UseCaseDiagram(ctx.IDENTIFIER().getText()))

    # Exit a parse tree produced by UMLParser#useCaseDiagram.
    def exitUseCaseDiagram(self, ctx: UMLParser.UseCaseDiagramContext):
        pass

    # Enter a parse tree produced by UMLParser#actor.
    def enterActor(self, ctx: UMLParser.ActorContext):
        name = ctx.IDENTIFIER().getText()
        if self.image.diagram.get_actor_by_name(name) is not None:
            raise Exception(f"Actor {name} already exists")

        self.image.diagram.add_actor(name)

    # Exit a parse tree produced by UMLParser#actor.
    def exitActor(self, ctx: UMLParser.ActorContext):
        pass

    # Enter a parse tree produced by UMLParser#useCaseStatement.
    def enterUseCaseStatement(self, ctx: UMLParser.UseCaseStatementContext):
        pass

    # Exit a parse tree produced by UMLParser#useCaseStatement.
    def exitUseCaseStatement(self, ctx: UMLParser.UseCaseStatementContext):
        pass

    # Enter a parse tree produced by UMLParser#useCaseDeclaration.
    def enterUseCaseDeclaration(self, ctx: UMLParser.UseCaseDeclarationContext):
        pass

    # Exit a parse tree produced by UMLParser#useCaseDeclaration.
    def exitUseCaseDeclaration(self, ctx: UMLParser.UseCaseDeclarationContext):
        name = ctx.IDENTIFIER().getText()
        if self.image.diagram.get_usecase_by_name(name) is not None:
            raise Exception(f"Use case {name} already exists")
        
        self.image.diagram.add_usecase(
            name, ctx.STRING().getText()[1:-1])

    # Enter a parse tree produced by UMLParser#dependency.
    def enterDependency(self, ctx: UMLParser.DependencyContext):

        if ctx.dependencyOperator().getText() == "--":
            actor = self.image.diagram.get_actor_by_name(
                str(ctx.IDENTIFIER()[0]))
            if actor is None:
                actor = self.image.diagram.get_actor_by_name(
                    str(ctx.IDENTIFIER()[1]))

            usecase = self.image.diagram.get_usecase_by_name(
                str(ctx.IDENTIFIER()[0]))
            if usecase is None:
                usecase = self.image.diagram.get_usecase_by_name(
                    str(ctx.IDENTIFIER()[1]))
            if usecase is None or actor is None:
                raise Exception("Invalid association")

            self.image.diagram.add_association(actor, usecase)
        else:
            left = self.image.diagram.get_usecase_by_name(
                str(ctx.IDENTIFIER()[0]))
            right = self.image.diagram.get_usecase_by_name(
                str(ctx.IDENTIFIER()[1]))
            if left is None:
                raise Exception(f"Usecase {ctx.IDENTIFIER()[0]} does not exist")
            if right is None:
                raise Exception(f"Usecase {ctx.IDENTIFIER()[1]} does not exist")
            if ctx.IDENTIFIER(0).getText() == ctx.IDENTIFIER(1).getText():
                raise Exception(f"Invalid dependency - usecase {ctx.IDENTIFIER(0).getText()} cannot depend on itself")

            match ctx.dependencyOperator().getText():
                case "-i>":
                    self.image.diagram.add_relation(left, right, "include")
                case "-e>":
                    self.image.diagram.add_relation(left, right, "extend")
                case "<i-":
                    self.image.diagram.add_relation(right, left, "include")
                case "<e-":
                    self.image.diagram.add_relation(right, left, "extend")

    # Exit a parse tree produced by UMLParser#dependency.
    def exitDependency(self, ctx: UMLParser.DependencyContext):
        pass

    # Enter a parse tree produced by UMLParser#dependencyOperator.
    def enterDependencyOperator(self, ctx: UMLParser.DependencyOperatorContext):
        pass

    # Exit a parse tree produced by UMLParser#dependencyOperator.
    def exitDependencyOperator(self, ctx: UMLParser.DependencyOperatorContext):
        pass

    # Enter a parse tree produced by UMLParser#package.
    def enterPackage(self, ctx: UMLParser.PackageContext):
        pass

    # Exit a parse tree produced by UMLParser#package.
    def exitPackage(self, ctx: UMLParser.PackageContext):
        pass

    # Enter a parse tree produced by UMLParser#sequenceDiagram.
    def enterSequenceDiagram(self, ctx: UMLParser.SequenceDiagramContext):
        self.image = UMLImage(SequenceDiagram(ctx.IDENTIFIER()))

    # Exit a parse tree produced by UMLParser#sequenceDiagram.
    def exitSequenceDiagram(self, ctx: UMLParser.SequenceDiagramContext):
        pass

    # Enter a parse tree produced by UMLParser#lifeline.
    def enterLifeline(self, ctx: UMLParser.LifelineContext):
        name = ctx.IDENTIFIER().getText()
        if self.image.diagram.get_lifeline_by_name(name) is not None:
            raise Exception(f"Lifeline {name} already exists")
        
        self.image.diagram.add_lifeline(name)

    # Exit a parse tree produced by UMLParser#lifeline.
    def exitLifeline(self, ctx: UMLParser.LifelineContext):
        pass

    # Enter a parse tree produced by UMLParser#seqStatement.
    def enterSeqStatement(self, ctx: UMLParser.SeqStatementContext):
        pass

    # Exit a parse tree produced by UMLParser#seqStatement.
    def exitSeqStatement(self, ctx: UMLParser.SeqStatementContext):
        pass

    # Enter a parse tree produced by UMLParser#action.
    def enterAction(self, ctx: UMLParser.ActionContext):
        source_name = ""
        target_name = ""
        type_ = ""
        name = ctx.STRING().getText() if ctx.STRING() else ""

        match ctx.actionType().getText():
            case "==>":
                source_name = ctx.IDENTIFIER(0).getText()
                target_name = ctx.IDENTIFIER(1).getText()
                type_ = "sync"
            case "<==":
                source_name = ctx.IDENTIFIER(1).getText()
                target_name = ctx.IDENTIFIER(0).getText()
                type_ = "sync"
            case "..>":
                source_name = ctx.IDENTIFIER(0).getText()
                target_name = ctx.IDENTIFIER(1).getText()
                type_ = "return"
            case "<..":
                source_name = ctx.IDENTIFIER(1).getText()
                target_name = ctx.IDENTIFIER(0).getText()
                type_ = "return"
            case "-*>":
                source_name = ctx.IDENTIFIER(0).getText()
                target_name = ctx.IDENTIFIER(1).getText()
                type_ = "async"
            case "<*-":
                source_name = ctx.IDENTIFIER(1).getText()
                target_name = ctx.IDENTIFIER(0).getText()
                type_ = "async"

        if self.image.diagram.get_lifeline_by_name(source_name) is None:
            raise Exception(f"Lifeline {source_name} does not exist")
        
        if self.image.diagram.get_lifeline_by_name(target_name) is None:
            raise Exception(f"Lifeline {target_name} does not exist")

        source = self.image.diagram.get_lifeline_by_name(source_name)
        target = self.image.diagram.get_lifeline_by_name(target_name)

        self.image.diagram.add_message(
            source,
            target,
            type_,
            name
        )

    # Exit a parse tree produced by UMLParser#action.
    def exitAction(self, ctx: UMLParser.ActionContext):
        pass

    # Enter a parse tree produced by UMLParser#actionType.
    def enterActionType(self, ctx: UMLParser.ActionTypeContext):
        pass

    # Exit a parse tree produced by UMLParser#actionType.
    def exitActionType(self, ctx: UMLParser.ActionTypeContext):
        pass

    # Enter a parse tree produced by UMLParser#actionOperator.
    def enterActionOperator(self, ctx: UMLParser.ActionOperatorContext):
        pass

    # Exit a parse tree produced by UMLParser#actionOperator.
    def exitActionOperator(self, ctx: UMLParser.ActionOperatorContext):
        pass

    # Enter a parse tree produced by UMLParser#actionsBlock.
    def enterActionsBlock(self, ctx: UMLParser.ActionsBlockContext):
        pass

    # Exit a parse tree produced by UMLParser#actionsBlock.
    def exitActionsBlock(self, ctx: UMLParser.ActionsBlockContext):
        pass

    # Enter a parse tree produced by UMLParser#alt.
    def enterAlt(self, ctx: UMLParser.AltContext):
        pass

    # Exit a parse tree produced by UMLParser#alt.
    def exitAlt(self, ctx: UMLParser.AltContext):
        pass

    # Enter a parse tree produced by UMLParser#opt.
    def enterOpt(self, ctx: UMLParser.OptContext):
        pass

    # Exit a parse tree produced by UMLParser#opt.
    def exitOpt(self, ctx: UMLParser.OptContext):
        pass

    # Enter a parse tree produced by UMLParser#par.
    def enterPar(self, ctx: UMLParser.ParContext):
        pass

    # Exit a parse tree produced by UMLParser#par.
    def exitPar(self, ctx: UMLParser.ParContext):
        pass

    # Enter a parse tree produced by UMLParser#critical.
    def enterCritical(self, ctx: UMLParser.CriticalContext):
        pass

    # Exit a parse tree produced by UMLParser#critical.
    def exitCritical(self, ctx: UMLParser.CriticalContext):
        pass

    # Enter a parse tree produced by UMLParser#forLoop.
    def enterForLoop(self, ctx: UMLParser.ForLoopContext):
        pass

    # Exit a parse tree produced by UMLParser#forLoop.
    def exitForLoop(self, ctx: UMLParser.ForLoopContext):
        pass

    # Enter a parse tree produced by UMLParser#whileLoop.
    def enterWhileLoop(self, ctx: UMLParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by UMLParser#whileLoop.
    def exitWhileLoop(self, ctx: UMLParser.WhileLoopContext):
        pass

    # Enter a parse tree produced by UMLParser#instruction.
    def enterInstruction(self, ctx: UMLParser.InstructionContext):
        pass

    # Exit a parse tree produced by UMLParser#instruction.
    def exitInstruction(self, ctx: UMLParser.InstructionContext):
        pass

    # Enter a parse tree produced by UMLParser#condition.
    def enterCondition(self, ctx: UMLParser.ConditionContext):
        pass

    # Exit a parse tree produced by UMLParser#condition.
    def exitCondition(self, ctx: UMLParser.ConditionContext):
        pass

    # Enter a parse tree produced by UMLParser#booleanOperator.
    def enterBooleanOperator(self, ctx: UMLParser.BooleanOperatorContext):
        pass

    # Exit a parse tree produced by UMLParser#booleanOperator.
    def exitBooleanOperator(self, ctx: UMLParser.BooleanOperatorContext):
        pass


del UMLParser
